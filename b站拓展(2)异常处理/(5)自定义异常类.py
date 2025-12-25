#继承Exception类
class MyCustomError(Exception):
    pass #无额外属性/方法,复用父类逻辑

#使用:通过raise语句触发
try:
    age=int(input('请输入您的年龄:'))
    if age<0 or age>120:
        raise MyCustomError(f'年龄非法:{age},请输入0-120之内的数值')
    else:
        print(f'f您的年龄为{age}')
except MyCustomError as e:
    print(e)