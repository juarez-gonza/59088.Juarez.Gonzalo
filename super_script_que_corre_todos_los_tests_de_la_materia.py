#! /usr/bin/python3
import os
import re

for root, dirs, files in os.walk("."):
    for f in files:
        if re.match("^test.*", f):
            test_path = os.path.join(root, f)
            os.system(f"coverage run --append {test_path}")

exit(0)
