#个数可变的位置参数
def fun(*para):
    print(type(para))
    for item in para:
        print(item)

#调用
fun(10,20,30,40)
fun([10,20,30,40])  #实际上传递的是一个参数
#在调用时,参数前加一颗星,会将列表进行解包
fun(*[10,20,30,40])



#个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key, value in kwpara.items():
        print(f'{key}:{value}')

#调用
fun2(name='曹云涛',age=18,height=170)

d={'name':'曹云涛','age':18,'height':170}
# fun2(d)         #TypeError: fun2() takes 0 positional arguments but 1 was given

fun2(**d)