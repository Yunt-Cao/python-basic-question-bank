lst=[54,77,95,56]
#(1)排序操作
asc_lst=sorted(lst)    #默认升序
desc_lst=sorted(lst,reverse=True) #降序
print(asc_lst)
print(desc_lst)

#reversed 反向
new_lst=reversed(lst)
print(new_lst)  #结果是迭代器对象，需要转换
print(list(new_lst))

#(3)zip
x=['a','b','c','d']
y=[10,20,30,40,50]
zip_object=zip(x,y)
print(zip_object)
#print(list(zip_object))

#(4)enumerate
enum=enumerate(y,start=1)
print(type(enum))
print(tuple(enum))

#(5)all
lst2=[11,'',55]
print(all(lst2))
print(any(lst2))

#(6)next
print(next(zip_object))
print(next(zip_object))
print(next(zip_object))

#(7)filter过滤/筛选函数
def fun(num):
    return  num%2==1    #可能是True 可能是False

obj=filter(fun,range(10))
print(list(obj))

#(8)map
def upper(x):
    return x.upper()

new_lst2=['hello','world','python']
obj2=map(upper,new_lst2)
print(list(obj2))