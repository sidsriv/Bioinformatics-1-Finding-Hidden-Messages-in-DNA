__author__ = 'Siddhant Srivastava'

import sys

Genome = sys.argv[1]
#with open(sys.argv[1], 'r') as fp:
#           Genome = fp.readline().strip('\n')


def Skew(Genome):
    
    skew = [0]

    for i in range(0, len(Genome)):
        if Genome[i] == 'C':
            skew.append(skew[i] - 1)
        elif Genome[i] == 'G':
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    return skew

def min_skew(Genome):
    skew = Skew(Genome)
    minimum = min(skew)
    return [i for i, val in enumerate(skew) if val == minimum]


ans = min_skew(Genome)

for num in ans:
    print num,

