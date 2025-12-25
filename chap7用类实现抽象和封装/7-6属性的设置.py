class Student:
    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender  #self.__gender是私有的实例属性

    #使用@property 修改方法,将方法转成属性使用
    @property
    def gender(self):
        return self.__gender


    #将我们的gender属性设置为可写属性
    @gender.setter
    def gender(self,value):
        if value!='男' and value!='女':
            print('性别有误,已将默认性别设置为男')
            self.__gender = '男'
        else:
            self.__gender = value


stu=Student('曹云涛','男')
print(stu.name,'的性别是',stu.gender)   #stu.gender就会去执行stu.gender()
#尝试修改属性值
#stu.gender='男' AttributeError: property 'gender' of 'Student' object has no setter不可重新赋值


stu.gender='帅哥'
print(stu.name,'的性别是',stu.gender)