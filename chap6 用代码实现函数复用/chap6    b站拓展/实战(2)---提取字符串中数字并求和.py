def get_digit(x):
    s=0 #存储累加和
    lst=[] #储存提取出来的数字
    for item in x:
        if item.isdigit():
            lst.append(int(item))
    #求和
    total=sum(lst)
    return lst,total

#函数的调用
s=input('请输入一个字符串:')
#调用
lst,total=get_digit(s)
print(lst)
print(total)