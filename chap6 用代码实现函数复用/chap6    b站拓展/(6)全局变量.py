a=100   #全局变量


def calc(x,y):
    return a+x+y
print(a)
print(calc(10,20))

print('-'*100)
def calc2(x,y):
    a=200      #局部
    return x+y+a
print(calc2(10,20))
print(a)    #输出的是全局变量的a

print('-'*100)
def calc3(x,y):
    global s
    s=300
    return x+y+s
print(calc3(10,20))
print(s)