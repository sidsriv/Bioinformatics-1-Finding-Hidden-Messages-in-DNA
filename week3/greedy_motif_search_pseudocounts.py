import sys


file_name = sys.argv[1]

dna = []
global k,t


with open(file_name) as f:
	for line in f:
		if len(line.split()) > 1:
			k,t = map(int,line.split())
		else:
			dna.append(line[:-1])

def count_with_pseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def profile_with_pseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile = count_with_pseudocounts(Motifs)
    for symbol in 'ACGT':
        for j in range(k):
            profile[symbol][j] = profile[symbol][j]/float(t+4)
    return profile

def consensus(Motifs):
    
    k = len(Motifs[0])
    counts = count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if counts[symbol][j] > m:
                m = counts[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def score(Motifs):
    profile = count(Motifs)
    Consensus = consensus(Motifs)
    t = len(Motifs)
    score = 0
    for i in range(len(Motifs[0])):
        score = score + (t - profile[Consensus[i]][i])
    return score

def pr(Text, Profile):
    pr = 1
    for i in range(len(Text)):
        pr = pr*Profile[Text[i]][i]
    return pr

def profile_most_probable_pattern(Text, Profile):
    T = len(Text)
    K = len(Profile['A'])
    prob = 0
    x = Text[0:K]
    for i in range(T - K + 1):
        Subtext = Text[i:i+K]
        temp_prob = pr(Subtext,Profile)
        if temp_prob > prob:
            prob = temp_prob
            x = Subtext
    return x

def greedy_motif_search_pseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = profile_with_pseudocounts(Motifs[0:j])
            Motifs.append(profile_most_probable_pattern(Dna[j], P))
        if score(Motifs) < score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


if __name__ == '__main__':
	ans = greedy_motif_search_pseudocounts(dna,k,t)
	for result in ans:
		print result
