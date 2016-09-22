import sys

seq1 = sys.argv[1]
seq2 = sys.argv[2]



def hamming_distance(genome1,genome2):
	score = 0
	if len(genome1) != len(genome2):
		print("Error")
	else:
		for i in range(len(genome1)):
			if genome1[i] != genome2[i]:
				score += 1
	return score

if __name__ == '__main__':
	ans = hamming_distance(seq1,seq2)
	print(ans)