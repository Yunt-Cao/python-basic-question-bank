a=10
b=20
print(dir(a)) #Python中一切皆对象
print(a+b)
print(a.__add__(b))
print(a.__sub__(b))
print('-'*50)
#小于
print(f'{a}<{b}吗？',a.__lt__(b))
print(f'{a}<={b}吗？',a.__le__(b))
print('-'*50)
#相等
print(a.__eq__(b))
#不相等
print(a.__ne__(b))
print('-'*50)
#大于和大于等于
print(a.__gt__(b))
print(a.__ge__(b))
print('-'*50)

#乘法和除法
print(a.__mul__(b))
print(a.__truediv__(b))     #非整除
print(a.__mod__(b))         #求余数
print(a.__floordiv__(b))    #整除
print('-'*50)

#幂运算
print(a.__pow__(b))
print('-'*50)

#转换为str类型
print(b.__str__())

#打印
print(b.__repr__())
print('-'*50)


