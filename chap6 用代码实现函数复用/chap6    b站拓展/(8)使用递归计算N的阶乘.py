def fac(n): #n的阶乘
    if n==1:
        return 1
    else:
        return n*fac(n-1) #自己调用自己(递归操作)

print(fac(5))