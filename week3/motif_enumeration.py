__author__ = 'Siddhant Srivastava'

import sys
from collections import defaultdict
from itertools import combinations, product, izip


file_name = sys.argv[1]

dna = []
global k,d


with open(file_name) as f:
	for line in f:
		if len(line.split()) > 1:
			k,d = map(int,line.split())
		else:
			dna.append(line[:-1])

alt_bases = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
def kmer_mismatches(kmer, d):
    mismatches = [kmer] 
    if d== 0:
    	return mismatches
	
    for dist in xrange(1, d+1):
        for change_indices in combinations(xrange(len(kmer)), dist):
            for substitutions in product(*[alt_bases[kmer[i]] for i in change_indices]):
                new_mistmatch = list(kmer)
                for idx, sub in izip(change_indices, substitutions):
                    new_mistmatch[idx] = sub
                mismatches.append(''.join(new_mistmatch))
    return mismatches




def motif_enumeration(dna, k, d):
    motif_sets = [{kmer for i in xrange(len(seq)-k+1) for kmer in kmer_mismatches(seq[i:i+k], d)} for seq in dna]
    return sorted(list(reduce(lambda a,b: a & b, motif_sets)))	    

if __name__ == '__main__':
	ans = motif_enumeration(dna,k,d)
	print(" ".join(str(x) for x in list(ans)))	
	print len(ans)