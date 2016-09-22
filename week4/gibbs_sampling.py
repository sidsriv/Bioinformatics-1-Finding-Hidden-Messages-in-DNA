import sys
from random import randint

file_name = sys.argv[1]

dna = []
global k,t,n


with open(file_name) as f:
	for line in f:
		if len(line.split()) > 1:
			k,t,n = map(int,line.split())
		else:
			dna.append(line[:-1])

def HammingDistance(genome1,genome2):
	score = 0
	if len(genome1) != len(genome2):
		print("Error")
	else:
		for i in range(len(genome1)):
			if genome1[i] != genome2[i]:
				score += 1
	return score

def score(motifs):
	score = 0
	for i in xrange(len(motifs[0])):
		motif = ''.join([motifs[j][i] for j in xrange(len(motifs))])
		score += min([HammingDistance(motif, homogeneous*len(motif)) for homogeneous in 'ACGT'])
	return score

def profile(motifs):
	prof = []
	for i in xrange(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in xrange(len(motifs))])
		prof.append([float(col.count(nuc))/float(len(col)) for nuc in 'ACGT'])
	return prof

def profile_most_probable_kmer(dna, k, prof):
	nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}
	max_prob = [-1, None]
	for i in xrange(len(dna)-k+1):
		current_prob = 1
		for j, nucleotide in enumerate(dna[i:i+k]):
			current_prob *= prof[j][nuc_loc[nucleotide]]
		if current_prob > max_prob[0]:
			max_prob = [current_prob, dna[i:i+k]]

	return max_prob[1]

def profile_with_pseudocounts(motifs):
	prof = []
	for i in xrange(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in xrange(len(motifs))])
		prof.append([float(col.count(nuc)+1)/float(len(col)+4) for nuc in 'ACGT'])
	return prof

def motifs_from_profile(profile, dna, k):
	return [profile_most_probable_kmer(seq,k,profile) for seq in dna]

def gibbs_sampler(dna_list,k,t,N):
	rand_ints = [randint(0,len(dna[0])-k) for a in xrange(t)]
	motifs = [dna_list[i][r:r+k] for i,r in enumerate(rand_ints)]
	best_score = [score(motifs), motifs]
	for i in xrange(N):
		r = randint(0,t-1)
		current_profile = profile_with_pseudocounts([motif for index, motif in enumerate(motifs) if index!=r])
		motifs = [profile_most_probable_kmer(dna[index],k,current_profile) if index == r else motif for index,motif in enumerate(motifs)]
		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]

	return best_score

if __name__ == '__main__':
	best_motifs = [k*t, None]
	for repeat in xrange(20):
		current_motifs = gibbs_sampler(dna,k,t,n)
		if current_motifs[0] < best_motifs[0]:
			best_motifs = current_motifs
	for seq in best_motifs[1]:
		print seq