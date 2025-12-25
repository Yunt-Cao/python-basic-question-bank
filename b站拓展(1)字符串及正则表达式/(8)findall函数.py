import re
pattern='\d\.\d+'
s='I study Python3.11 everyday Python2.7 I love you'
s2='4.10 Python I study every day'
lst=re.findall(pattern,s)
lst2=re.findall(pattern,s2)
print(lst)
print(lst2)