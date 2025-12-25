d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d)  #key相同时value进行了覆盖

#zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo']
x=zip(lst1,lst2)
print(x)
# print(list(x))
d=dict(x)
print(d)

#使用参数创建字典
d=dict(cat=10,dog=20,pet=30,zoo=40)
print(d)

t=(10,20,30,40)
print({t:10})  #元组t可以是key

del d['cat']
print(d)