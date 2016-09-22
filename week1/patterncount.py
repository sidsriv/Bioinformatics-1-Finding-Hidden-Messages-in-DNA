import sys

text = sys.argv[1]
pattern = sys.argv[2]

def count(text,pattern):
	count = 0
	for i in range(len(text) - len(pattern) + 1):
		if text[i:i+len(pattern)] == pattern:
			count += 1
	return count

ans = count(text,pattern)

print(ans)

