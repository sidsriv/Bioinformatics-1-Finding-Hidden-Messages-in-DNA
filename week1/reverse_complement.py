import sys

text = sys.argv[1]

def reverse_comp(sequence):
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
	

ans = reverse_comp(text)

print(ans)