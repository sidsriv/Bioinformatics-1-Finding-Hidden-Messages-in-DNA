__author__ = 'Siddhant Srivastava'

import sys

file_name = sys.argv[1]

lines = []



with open(file_name) as f:
	for line in f:
		lines.append(line[:-1])
	

k = int(lines[0])
dna = lines[1:]


numbertosymbol = {0:'A', 1:'C', 2:'G', 3:'T'}

def hamming_distance(genome1,genome2):
	score = 0
	if len(genome1) != len(genome2):
		print("Error")
	else:
		for i in range(len(genome1)):
			if genome1[i] != genome2[i]:
				score += 1
	return score

def numbertopattern(index, k):
	if k == 1:
		return numbertosymbol[index]
	prefixindex = index / 4
	r = index % 4
	prefixpattern = numbertopattern(prefixindex, k - 1)
	return prefixpattern + numbertosymbol[r]

def distance_between_pattern_and_string(pattern,dna):
	k = len(pattern)
	distance = 0
	for seq in dna:
		hamming_score = 100
		for i in range(len(seq)- k + 1):
		    if hamming_score > hamming_distance(pattern,seq[i:i+k]):
		    	hamming_score = hamming_distance(pattern,seq[i:i+k])
		distance += hamming_score
	return distance

def median_string(dna,k):
	distance = 100
	median = ''
	for i in range(4**k):
		pattern = numbertopattern(i,k)
		if distance > distance_between_pattern_and_string(pattern,dna):
			distance = distance_between_pattern_and_string(pattern,dna)
			median = pattern
	return median


if __name__ == '__main__':
	ans = median_string(dna,k)
	print ans