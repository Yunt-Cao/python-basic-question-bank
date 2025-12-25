class Student:
    #类属性:定义在类中,方法外的变量
    school='大冶一中教育'

    #初始化方法
    def __init__(self,xm,age):#xm,age是方法的参数,是局部变量,xm,age的作用域是整个__init__方法
        self.name=xm  #左侧是实例属性,xm是局变量,将局部变量的值xm,age的作用域是整个__init__方法
        self.age=age #实例的名称和局部变量的名称可以相同

#定义在类中的函数叫方法,自带一个参数self
    def show(self):
        print(f'我叫:{self.name},今年:{self.age}了')

#根据'图纸'可以创建N多个对象
stu=Student('cyt',18)
stu2=Student('pyt',18)
stu3=Student('lzy',18)
stu4=Student('cwh',18)

print(stu)
print(stu2)
print(stu3)
print(stu4)

lst=[stu,stu2,stu3,stu4]
for item in lst:
    #对象名打点调用
    item.show()