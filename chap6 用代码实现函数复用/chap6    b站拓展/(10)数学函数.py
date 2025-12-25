#(1)abs---绝对值
print(abs(-9))

#(2)    divmod--返回两个数值的商和余数
print(divmod(10,3))

#(3)max--最大值
print(max('hello'))
print(max(-9,6,8,key=abs))
print(max([10,-9,-95],key=abs))

#sum求和
lst=[11,44]
lst2=[55,100,45]
print('求和:',sum(lst))
print([10,85,5])

#pow函数
print('x的y次幂:',pow(2,8))

#四舍五入---默认成整数
print(round(3.1415926535))
print(round(3.1415926535,2))    #保留两位小数
print(round(3.1415926535,-1))
print(round(314.1415926535,-1)) #-1对个位上进行四舍五入