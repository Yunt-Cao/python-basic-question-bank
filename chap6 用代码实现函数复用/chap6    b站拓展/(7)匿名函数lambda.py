def calc(a,b):
    return a+b
print(calc(10,20))


#匿名函数
s=lambda a,b:a+b    #s表示就是一个匿名函数
print(type(s)) #<class 'function'> 函数
#调用匿名函数
print(s(10,20))
print('-'*100)

#列表的正常取值
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])

print('-'*100)

#lambda
for i in range(len(lst)):
    result=lambda x:x[i]    #根据索引取值,result的类型是函数
    print(result(lst))


#
student_scores=[
    {'name':'曹云涛','score':100},
    {'name':'叫大家','score':80},
    {'name':'大苏打','score':85},
]
#对列表进行排序，按成绩
student_scores.sort(key=lambda x:x['score'],reverse=True)#降序
print(student_scores)
