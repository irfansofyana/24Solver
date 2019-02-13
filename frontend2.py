from backend import *
import sys
import re

inFile = sys.argv[1]
outFile = sys.argv[2]

sol = []

with open(inFile,'r+') as i:
    lines = i.readline()

array = [int(s) for s in lines.split() if s.isdigit()]
Solve(array,sol)
lines = str(array[0]) + str(sol[0]) + str(array[1]) + str(sol[1]) + str(array[2]) + str(sol[2]) + str(array[3]) + "=" + str(sol[3])
with open(outFile,'w') as o:
    for line in lines:
        o.write(line)