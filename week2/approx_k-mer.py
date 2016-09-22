import sys

seq1 = sys.argv[1]
seq2 = sys.argv[2]
num = int(sys.argv[3])


def hamming_distance(genome1,genome2):
	score = 0
	if len(genome1) != len(genome2):
		print("Error")
	else:
		for i in range(len(genome1)):
			if genome1[i] != genome2[i]:
				score += 1
	return score

def approx_matching(kmer,genome,hamming_score):
	start_points = []
	for i in range(len(genome) - len(kmer) + 1):
		score = hamming_distance(kmer,genome[i:i+len(kmer)])
		if hamming_score>=score:
			start_points.append(i)
	return start_points

if __name__ == '__main__':
	ans = approx_matching(seq1,seq2,num)
	for num in ans:
		print num,