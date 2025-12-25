#search搜索第一个匹配的值

import re
pattern='\d\.\d+'
s='I study Python3.11 everyday Python2.7 I love you'
match=re.search(pattern,s)
print(match)



s2='4.10 Python I study every day'
match2=re.search(pattern,s2)
print(match2)

print(match2.group())
