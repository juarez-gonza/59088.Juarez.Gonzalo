#! /usr/bin/python3

# Hace lo mismo que su version en shell nada mas
# que no me había acordado de la existencia del comando
# find en shell pero sí de os.walk en el momento
# que se me ocurrio automatizar esto jejox

import os
import re

for root, dirs, files in os.walk("."):
    for f in files:
        if re.match("^test.*", f):
            test_path = os.path.join(root, f)
            cmd = "coverage run --append "+test_path
            os.system(cmd)

exit(0)
