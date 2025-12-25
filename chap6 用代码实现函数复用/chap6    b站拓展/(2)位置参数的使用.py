#位置传参
def happy_birthday(name,age):
    print('祝'+name+'生日快乐!')
    print(str(age)+'生日快乐')

#调用
happy_birthday('曹云涛',18)

#关键字传参
happy_birthday(age=18,name='曹云涛')


#默认值传参
def happy_birthday(name='曹云涛',age='18'):
    print('祝' + name + '生日快乐!')
    print(str(age) + '生日快乐')
#调用
happy_birthday()
happy_birthday('曹志祥')
happy_birthday(age='18')

def fun(a,b=20):
    pass

#当位置参数和关键字参数同时存在的时候,应该遵循,位置参数在前,默认参数在后