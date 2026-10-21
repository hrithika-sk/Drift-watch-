import os
import re
import shutil

with open("README.md") as f:
    text = f.read()

claims = re.findall(r"`([^`]+)`", text)

total = 0
passed = 0

for item in claims:
    if " " in item:
        ok = shutil.which(item.split()[0]) is not None
        label = "CMD"
    elif "." in item:
        ok = os.path.exists(item)
        label = "FILE"
    else:
        continue

    total += 1

    if ok:
     passed += 1
     print(("PASS " if ok else "FAIL ") + label + " " + item)

if total:
    score = round(100 * passed / total)
    print()
    print(f"Drift Score: {score}/100  ({passed} of {total} claims true)")