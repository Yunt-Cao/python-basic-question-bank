class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #方法重写
    def __str__(self):
        return '这是一个人,具有name和age两个实例属性' # 返回值是一个字符串

#创建Person类的对象
per=Person('曹志祥',49)
print(per)      #直接输出对象名,实际上是调用__str__方法
print(per.__str__())    # 手动调用
