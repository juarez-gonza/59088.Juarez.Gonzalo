#! /usr/bin/python3
import os
import re

for root, dirs, files in os.walk("."):
    for f in files:
        if re.match("^test.*", f):
            test_path = os.path.join(root, f)
            cmd = "coverage run --source="+root+" --append "+test_path
            os.system(cmd)

exit(0)
