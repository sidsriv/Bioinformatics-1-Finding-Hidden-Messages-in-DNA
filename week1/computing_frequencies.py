import sys

text = sys.argv[1]
k = int(sys.argv[2])

numbertosymbol = {0:'A', 1:'C', 2:'G', 3:'T'}
symboltonumber = {'A':0, 'C':1, 'G':2, 'T':3}

def numbertopattern2(n, k):
	pattern = [numbertosymbol[0] for el in range(k)]
	for i in range(k - 1, -1, -1):
		pattern[i]= numbertosymbol[n % 4]
		n /= 4
	return ''.join(pattern)
		    
def numbertopattern(index, k):
	if k == 1:
		return numbertosymbol[index]
	prefixindex = index / 4
	r = index % 4
	prefixpattern = numbertopattern(prefixindex, k - 1)
	return prefixpattern + numbertosymbol[r]

def patterntonumber(pattern):
	if len(pattern)  == 0:
		return 0
	return 4 * patterntonumber(pattern[:-1]) + symboltonumber[pattern[-1]]

def compute_frequency(text,k):
	freq_arr = [0 for _ in xrange(4**k)]
	for i in xrange(len(text) - k + 1):
		pattern = text[i:i+k]
		j = patterntonumber(pattern)
		freq_arr[j] = freq_arr[j] + 1
	return freq_arr

