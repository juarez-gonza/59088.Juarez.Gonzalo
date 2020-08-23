#! /bin/bash
find -iregex ".*/test.*\.py" -exec coverage run --append {} \;
