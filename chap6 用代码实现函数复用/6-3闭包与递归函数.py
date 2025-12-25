#闭包
def greeting_conf(prefix):
    def greeting(name):
        return print(prefix , name)
    return greeting

mGreeting=greeting_conf('Good Morning')
mGreeting('Wilbert')
mGreeting('Bob')

aGreeting=greeting_conf('Good Afternoon')
aGreeting('Mike')
aGreeting('Jordan')

#递归函数
def fib(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fib(i-1)+fib(i-2)
print(fib(8))  #fib(8)=fib(7)+fib(6)


#阶乘的迭代实现
def factorial(n):
    t=1
    for i in range(1,n+1):
        t*=i
    return t
print(factorial(8))

#阶乘的递归实现
def factorial2(n):
    if n==0:
        return 1
    else:
        return n*factorial2(n-1)
print(factorial2(8))
