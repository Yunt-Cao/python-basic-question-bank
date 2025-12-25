class A :
    pass
class B :
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

#创建类的对象
a=A()
b=B()
#创建C类的对象
c=C('曹云涛',20)

print('对象a的属性字典',a.__dict__)
print(b.__dict__)
print(c.__dict__)

print('-'*50)

print('对象a所属的类',a.__class__)
print(b.__class__)
print(c.__class__)

print('-'*50)

print('A类的父类元组：',A.__bases__)
print(B.__bases__)
print(C.__bases__)

print('-'*50)

print('A类的父类：',A.__base__)
print(B.__base__)
print(C.__base__)   #如果继承了N多个父类,结果只显示第一个父类

print('-'*50)

print('A类的层次结构',A.__mro__)
print(B.__mro__)
print(C.__mro__)    #C继承了A，B类，间接继承了object类
print('-'*50)

#子类列表
print('A的子类列表：',A.__subclasses__())
print(B.__subclasses__())
print(C.__subclasses__())   #没有子类空列表