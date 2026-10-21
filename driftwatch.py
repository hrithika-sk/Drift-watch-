
import os
import re
import shutil

with open("README.md") as f:
    text = f.read()

claims = re.findall(r"`([^`]+)`", text)

for item in claims:
    if " " in item:
        # looks like a command, e.g. `python driftwatch.py`
        tool = item.split()[0]
        found = shutil.which(tool) is not None
        print(("CMD OK   " if found else "CMD MISSING ") + item)
    elif "." in item:
        found = os.path.exists(item)
        print(("OK       " if found else "MISSING  ") + item)
