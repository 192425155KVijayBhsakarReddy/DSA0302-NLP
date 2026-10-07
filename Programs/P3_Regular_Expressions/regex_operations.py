import re

text = """Call me on 9876543210 or 9123456780.
Email: abc@gmail.com, xyz@yahoo.com.
Meeting on 12/10/2026. Contact Vijay."""

print("Date:", re.findall(r'\d{2}/\d{2}/\d{4}', text))
print("Mobile:", re.findall(r'\b[6-9]\d{9}\b', text))
print("Email:", re.findall(r'\w+@\w+\.\w+', text))
print("Capital words:", re.findall(r'\b[A-Z][a-z]*\b', text))
print("Starts with Call:", bool(re.match(r'Call', text)))

print("New date:", re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', text))
print("Hidden phone:", re.sub(r'\b[6-9]\d{9}\b', 'XXXXXXXXXX', text))
