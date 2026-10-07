from textblob import TextBlob

w = input("Enter word: ")
print("Corrected:", TextBlob(w).correct())
