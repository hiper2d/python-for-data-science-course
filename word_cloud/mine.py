import re
from collections import Counter

textFile = open('98-0.txt', encoding='utf-8')
excludeFile = open('stopwords', encoding='utf-8')
text = textFile.read().lower()
stopwords = excludeFile.read().lower().split()
words = Counter()

for word in re.findall(r'[^\s\.,"“”]+', text):
	if word not in stopwords:
		words[word] += 1

print(words.most_common(10))
