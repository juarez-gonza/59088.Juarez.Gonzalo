#! /bin/bash

# ughh si solo 1 linea de script mucho mas lindo
# que su version con os.walk en python

find -iregex ".*/test.*\.py" -exec coverage run --append {} \;

coverage report

exit 0
