import sys


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

with open("ns_" + sys.argv[1], 'w') as f:
    for l in lines:
        splts = l.split()
        splts[0] = str(int(float(splts[0])*1e9))
        f.write(' '.join(splts) + "\n")