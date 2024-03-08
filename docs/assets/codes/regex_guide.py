import re

text = "this is not great."
updated_text = re.sub("not (?!good)", 'fabulously ', text)
print(updated_text)


pattern = '(?P<quote>[\'"]).*(?P=quote)'
text = 'he hollered "hello"'
print(re.search(pattern, text))
# output <re.Match object; span=(12, 19), match='"hello"'>

pattern = 'I saw Mummy'
text = 'I saw Mummy kissing Santa'
print(re.match(pattern, text))
# ouput: <re.Match object; span=(0, 11), match='I saw Mummy'>

pattern = 'saw Mummy'
text = 'I saw Mummy kissing Santa'
print(re.match(pattern, text))
# output: None

pattern = 'saw Mummy'
text = 'I saw Mummy kissing Santa'
print(re.search(pattern, text))
# output: <re.Match object; span=(2, 11), match='saw Mummy'>

pattern = '([^\s]+(?P<duplicate>[^\s])(?P=duplicate)[^\s]+)'
text = 'I saw Mummy kissing Santa'
print(re.findall(pattern, text))
# output: [('Mummy', 'm'), ('kissing', 's')]

pattern = re.compile("\w{1,3}coin")
print(pattern.match('dogcoin'))
print(pattern.match('bitcoin'))
print(pattern.match('acoin'))

pattern = "number 4*0?"
text = "<number 44 is ten times less than number 440"
print(re.findall(pattern, text))


pattern = "<.*?>"
pattern2 = "<.*>"
html = "<a href=https://mipsmonsta.github.io>Cave of Mipsmonsta</a>"
print(re.findall(pattern, html))
# output: ['<a href=https://mipsmonsta.github.io>', '</a>']
print(re.findall(pattern2, html))
# output: ['<a href=https://mipsmonsta.github.io>Cave of Mipsmonsta</a>']

