import re

text = "this is not great."
updated_text = re.sub("not (?!good)", 'fabulously ', text)
print(updated_text)


pattern = '(?P<quote>[\'"]).*(?P=quote)'
text = 'he hollered "hello"'
print(re.search(pattern, text))
# output <re.Match object; span=(12, 19), match='"hello"'>