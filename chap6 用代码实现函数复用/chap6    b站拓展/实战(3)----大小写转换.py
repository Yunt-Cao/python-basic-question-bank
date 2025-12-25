s=input('请输入一个字符串:')
new_s=''
for i in range(len(s)):
    if s[i].isupper():
        new_s+=s[i].lower()
    elif s[i].islower():
        new_s+=s[i].upper()
    else:
        new_s+=s[i]
print(new_s)



#Unicode码
def lower_upper(x): #x是一个字符串,形式参数
    lst=[]
    for item in x:
        if 'A'<=item<='Z':
            lst.append(item.lower())
        elif 'a'<=item<='z':
            lst.append(item.upper())
        else:
            lst.append(item)
    return ''.join(lst)
x=input('请输入一个字符串:')
print(lower_upper(x))
