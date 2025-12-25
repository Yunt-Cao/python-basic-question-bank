#函数的返回值
def calc(a,b):
    print(a+b)

calc(10,20)
print(calc(1,2))  #None  不可直接输出函数，因为没有使用return去返回任何结果

def calc2(a,b):
    s=a+b
    return s

print('-'*100)
get_s=calc2(1,2)
print(get_s)
get_s2=calc2(calc2(1,2),3)
print(get_s2)

#返回值可以是多个
def get_sum(num):
    s=0  #累加和
    odd_num=0   #奇数和
    even_num=0  #偶数和
    for i in range (1,num+1):
        if i%2!=0:
            odd_num+=i
        else:
            even_num+=i
        s+=i
    return odd_num,even_num,s
result=get_sum(10)
print(type(result))
print(result)

#解包赋值
a,b,c=result
print(a,b,c)