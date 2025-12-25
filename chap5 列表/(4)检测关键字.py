python_keywords=('if','else','for','while','def','class','import','return')
word=input('请输入要检测的单词：')
if word in python_keywords:
    print(word,'是关键字')
else:
    print(word,'不是关键字')
