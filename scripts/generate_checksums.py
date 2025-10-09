#!/usr/bin/env python3
import hashlib, pathlib, datetime

root = pathlib.Path(__file__).resolve().parents[1]
targets = [
    "10_Research_Whitepapers",
    "20_Social_Contract",
    "30_Visual_Assets",
    "40_Publication_Packages"
]
log = root / "90_Administrative" / "Checksum_Log.txt"
now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

entries = []
for folder in targets:
    for p in pathlib.Path(root / folder).rglob("*"):
        if p.is_file():
            digest = sha256(p)
            rel = p.relative_to(root)
            entries.append(f"{now}  {digest}  {rel}")

log.parent.mkdir(parents=True, exist_ok=True)
with open(log, "a") as f:
    f.write("# Checksum batch {}\n".format(now))
    for e in entries:
        f.write(e + "\n")

print(f"Wrote {len(entries)} checksum entries to {log}")
