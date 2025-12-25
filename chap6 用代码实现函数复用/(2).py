str1=str(input('请输入句子：'))
def change(str1):
    result=[]
    for char in str1:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)
print(change(str1))