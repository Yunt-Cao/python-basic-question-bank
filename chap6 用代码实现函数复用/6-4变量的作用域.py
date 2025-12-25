#局部变量
def func1(x,y):
    x1=x
    y1=y
    z=100
    print('in func1(),x1=',x1)
    print('in func1(),y1=',y1)
    print('in func1(),z=',z)
    func2()
    return
def func2():
    x1=10
    y1=20
    z=0
    print('in func2(),x1=',x1)
    print('in func2(),y1=',y1)
    print('in func2(),z=',z)
func1('a','b')



#全局变量
#(1)
basis=100
def func1(x,y):
    sum=basis+x+y
    return sum

def func2(x,y):
    avg=(basis+x*0.9+y*0.8)/3
    return avg

score1=func1(75,62)
score2=func2(75,62)
print('{:6.2f},{:6.2f}'.format(score1,score2))
print(basis)
print('-'*1000)

#(2)
basis=100
def func3(x,y):
    basis=90
    sum=basis+x+y
    return sum
print('{:6.2f}'.format(func3(75,62)))
print(basis)
print('-'*1000)

#global语句
basis=100   #全局变量
def func4(x,y):
    global basis    #声明basis是函数外的全局变量
    print(basis)
    basis=90
    sum=basis+x+y
    return sum
print('{:6.2f}'.format(func4(75,62)))
print(basis)
print('-'*1000)