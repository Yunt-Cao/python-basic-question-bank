class Person():
    def eat(self):
        print('人,吃五谷杂粮')


class Cat():
    def eat(self):
        print('猫，喜欢吃鱼')

class Dog():
    def eat(self):
        print('狗,喜欢啃骨头')

#三个类中都有一个同名的方法---eat
#编写函数
def fun(obj):  #形式参数
    obj.eat()  # 通过变量obj(对象)调用eat方法


#创建三个类的对象
per=Person()
cat=Cat()
dog=Dog()


#调用fun函数
fun(per)
fun(cat)
fun(dog)