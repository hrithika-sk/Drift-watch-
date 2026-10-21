import os
import re

with open("README.md") as f:
    text = f.read()

# find anything written between backticks, like `utils/auth.py`
claims = re.findall(r"`([^`]+)`", text)

for item in claims:
    if "." in item:
        found = os.path.exists(item)
        print(("OK       " if found else "MISSING  ") + item)
