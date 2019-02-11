# import "gui.py"

import sys

inFile = sys.argv[1]
outFile = sys.argv[2]

with open(inFile,'r+') as i:
    lines = i.readline()

print(lines)
# processedLines = manipulateData(lines)

with open(outFile,'w') as o:
    for line in lines:
        o.write(line)