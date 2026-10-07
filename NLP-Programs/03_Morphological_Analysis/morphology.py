#3
import nltk
from nltk.stem import PorterStemmer

text = "playing played studies students"

words = text.split()

stemmer = PorterStemmer()

for word in words:
    print(word, "->", stemmer.stem(word))
