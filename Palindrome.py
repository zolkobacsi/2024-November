import re

my_text = "Madam madaM"
reverse_text = ""

lowercase_my_text = my_text.lower()

final_text = re.sub(r'[^a-zA-Z]', '', lowercase_my_text)

for i in reversed(final_text):
    reverse_text += i

if reverse_text != final_text:
    print("This is not a Palindrome!")
else:
    print("This is a Palindrome!")

