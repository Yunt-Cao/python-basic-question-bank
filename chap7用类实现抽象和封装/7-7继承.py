class Person:  #默认继承了object
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'大家好,我叫:{self.name},我今年:{self.age}岁了')

#Student继承Person类
class Student(Person):
    #编写初始化的方法
    def __init__(self,name,age,stuno):
        super().__init__(name,age) #调用父类的初始化方法
        self.stuno=stuno



class Doctor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department


#创建第一个子类对象
stu=Student('曹云涛',18,'2025001341')
stu.show()

doctor=Doctor('czx',49,'内科')
doctor.show()
