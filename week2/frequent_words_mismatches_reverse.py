import sys
from collections import defaultdict
from itertools import combinations, product, izip

seq1 = sys.argv[1]
kmer_num = int(sys.argv[2])
num = int(sys.argv[3])

def rev_comp(sequence):
	rev_comp = ''
	for nucleotide in sequence:
		if nucleotide == 'A':
			rev_comp = rev_comp + 'T'
		elif nucleotide == 'T':
			rev_comp = rev_comp + 'A'
		elif nucleotide == 'G':
			rev_comp = rev_comp + 'C'
		elif nucleotide == 'C':
			rev_comp = rev_comp + 'G'
	rev_comp = rev_comp[::-1]
	return rev_comp


def kmer_mismatches(kmer, d):
    mismatches = [kmer] 
    alt_bases = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
    for dist in xrange(1, d+1):
        for change_indices in combinations(xrange(len(kmer)), dist):
            for substitutions in product(*[alt_bases[kmer[i]] for i in change_indices]):
                new_mistmatch = list(kmer)
                for idx, sub in izip(change_indices, substitutions):
                    new_mistmatch[idx] = sub
                mismatches.append(''.join(new_mistmatch))
    return mismatches

def frequentwords_mismatches_reverse(seq, k, d):
    kmer_freq = defaultdict(int)
    for i in xrange(len(seq)-k+1):
        kmer_freq[seq[i:i+k]] += 1
        kmer_freq[rev_comp(seq[i:i+k])] += 1

    mismatch_count = defaultdict(int)
    for kmer, freq in kmer_freq.iteritems():
        for mismatch in kmer_mismatches(kmer, d):
            mismatch_count[mismatch] += freq
	
	max_count = max(mismatch_count.values())    
    return sorted([kmer for kmer, count in mismatch_count.iteritems() if count == max_count])

if __name__ == '__main__':
	ans = frequentwords_mismatches_reverse(seq1,kmer_num,num)
	print(" ".join(str(x) for x in list(ans)))	