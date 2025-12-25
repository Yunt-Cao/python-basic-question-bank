def hello():
    print("Hello World!")
    return
hello()

def circlearea(r):
    s=3.14*r*r
    return s
print(circlearea(eval(input('请输入圆的半径：'))))
print(circlearea(3))

#函数的嵌套
def sum(n):     #计算1！到n！的和
#计算a！的阶乘
    def fact(a):
        t=1
        for i in range(1,a+1):
            t*=i
        return t
    s=0
    for i in range(1,n+1):
        s+=fact(i)
    return s
n=5
print('{}以内的阶乘和为：{}'.format(n,sum(n)))

#函数的嵌套调用
def main():
    print('输入数据')
    userInput()
    print('处理数据')
    userProcessing()
    print('输出数据')
    userOutput()

def userInput():
    pass
def userProcessing():
    pass
def userOutput():
    pass

main()