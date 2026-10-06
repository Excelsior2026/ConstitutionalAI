"""Portable repository verification implemented with Dagger."""
from __future__ import annotations
from typing import Annotated
import dagger
from dagger import DefaultPath,dag,function,object_type
PYTHON_IMAGE="python:3.12-slim";NODE_IMAGE="node:20-bookworm-slim";GITLEAKS_IMAGE=("ghcr.io/gitleaks/gitleaks:v8.28.0@sha256:" "cdbb7c955abce02001a9f6c9f602fb195b7fadc1e812065883f695d1eeaba854");SOURCE=Annotated[dagger.Directory,DefaultPath("/")]
@object_type
class RepoCi:
 def _c(self,i,s):return dag.container().from_(i).with_directory("/src",s).with_workdir("/src")
 @function
 async def node(self,source:SOURCE)->str:
  s=r"""set -eu
found=0
for d in . web frontend ui app;do [ -f "$d/package.json" ]||continue;found=1;cd "/src/${d#./}";if [ -f pnpm-lock.yaml ];then corepack enable;pnpm install --frozen-lockfile;m=pnpm;elif [ -f yarn.lock ];then corepack enable;(yarn install --immutable||yarn install --frozen-lockfile);m=yarn;elif [ -f package-lock.json ]||[ -f npm-shrinkwrap.json ];then npm ci;m=npm;else npm install;m=npm;fi;h(){ node -e "const p=require('./package.json');process.exit(p.scripts&&p.scripts[process.argv[1]]?0:1)" "$1";};for n in lint test build;do if h "$n";then if [ "$n" = test ];then CI=true "$m" run "$n";else "$m" run "$n";fi;fi;done;if [ "$m" = npm ]&&{ [ -f package-lock.json ]||[ -f npm-shrinkwrap.json ];};then npm audit --omit=dev --audit-level=high;fi;done
[ "$found" -eq 1 ]||echo "node: skipped"
""";await self._c(NODE_IMAGE,source).with_exec(["sh","-lc",s]).stdout();return"node: passed or not applicable"
 @function
 async def python(self,source:SOURCE)->str:
  s=r"""set -eu
if [ ! -f pyproject.toml ]&&[ ! -f setup.py ]&&[ ! -f setup.cfg ]&&[ ! -f requirements.txt ];then echo "python: skipped";exit 0;fi
python -m pip install --upgrade pip
if [ -f pyproject.toml ]||[ -f setup.py ]||[ -f setup.cfg ];then python -m pip install -e ".[dev]"||python -m pip install -e .;else python -m pip install -r requirements.txt;fi
python -m pip install "pip-audit==2.7.3";python -m pip_audit --strict --local
if command -v ruff >/dev/null 2>&1;then ruff check .;fi
if command -v pytest >/dev/null 2>&1&&[ -d tests ];then pytest -q;fi
""";await self._c(PYTHON_IMAGE,source).with_exec(["sh","-lc",s]).stdout();return"python: passed or not applicable"
 @function
 async def production_image(self,source:SOURCE)->str:
  if "Dockerfile" not in await source.entries():return"production-image: skipped"
  i=source.docker_build(platform=dagger.Platform("linux/amd64"));await i.with_exec(["sh","-lc","true"]).stdout();return"production-image: passed"
 @function
 async def secrets(self,source:SOURCE)->str:
  c=dag.container().from_(GITLEAKS_IMAGE).with_directory("/src",source).with_workdir("/src").with_exec(["sh","-lc","test -d .git||exit 42"]).with_exec(["gitleaks","detect","--redact","-v","--source","."]);await c.stdout();return"secrets: passed"
 @function
 async def verify(self,source:SOURCE)->str:return"\n".join([await self.node(source),await self.python(source),await self.production_image(source),await self.secrets(source)])
