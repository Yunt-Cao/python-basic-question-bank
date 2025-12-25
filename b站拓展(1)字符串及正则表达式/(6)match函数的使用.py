#match提取开头数字


import re   #导入正则处理模块
pattern='\d\.\d+'   #+限定符，\d 0-9出现一次或多次
s='I study python 3.11 every day'
match=re.match(pattern,s,re.I)
print(match)    #None
s2='3.11Python I study every day'
match2=re.match(pattern,s2,)
print(match2)

print('匹配值的起始位置:',match2.start())
print('结束位置:',match2.end())
print('匹配区间的位置元素:',match2.span())
print('待匹配的字符串:',match2.string)
print('匹配的数据:',match2.group())