import os
import re
import sys

currentdir = os.getcwd()
targetstring = sys.argv[1]

pattern = r"(.*" + re.escape(targetstring) + "[^\\\\]+)"
regex = re.compile(pattern, re.IGNORECASE)
match = regex.search(currentdir)
if match:
    command = "cds " + os.path.abspath(match.group(1))
    print command
