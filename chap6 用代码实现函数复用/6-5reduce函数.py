from functools import reduce
r1=reduce(lambda x,y:x+y,(1,2,3,4,5))
print(r1)

#reduce()函数的第三个参数设置初值
r2=reduce(lambda x,y:x+y,(1,2,3,4,5),10000)
print(r2)

#生成整数数值
r3=reduce(lambda x,y:x*10+y,[1,2,3,4,5])
print(r3)

list1=[1,2,3,4,5]
sorted_list=sorted(list1,reverse=False)
print(sorted_list)

