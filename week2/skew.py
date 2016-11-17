__author__ = 'Siddhant Srivastava'

import sys

text = sys.argv[1]



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

ans = Skew(text)
for num in ans:
	print num,