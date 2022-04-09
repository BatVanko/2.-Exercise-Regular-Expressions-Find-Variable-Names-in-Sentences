import re

text = input()
pattern = r"\b_[a-zA-Z0-9]+\b"

result = re.findall(pattern,text)

word_list = []
for word in result:
    word_list.append(word)
print(",".join(word_list))




