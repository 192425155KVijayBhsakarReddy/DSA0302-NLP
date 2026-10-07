#1
import re

text = "I am studying NLP. My email is abc@gmail.com"

pattern = r'\w+@\w+\.\w+'

result = re.search(pattern, text)

if result:
    print("Email found:", result.group())
else:
    print("Email not found")
