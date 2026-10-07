#p1
import nltk
from collections import Counter

p = """NLP is a fascinating field.
NLP helps computers understand language.
NLP is used in many applications."""

s = sent_tokenize(p)
w = [x.lower() for x in word_tokenize(p) if x.isalnum()]

print("Sentences:", s)
print("Words:", w)
print("Count:", len(w))
print("Most common:", Counter(w).most_common(1))
