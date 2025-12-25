#{}直接创建集合
s={10,20,30,40}
print(s)

#集合只能储存不可变数据类型
# s={[10,20],[30,40]}
# print(s)

s=set()
print(s,type(s))

s=set('helloworld')
print(s)  #两个o编程了一个o  证明是无序且不重复的

s2=set([10,20,30])
print(s2)

s3=set(range(10))
print(s3)

#集合属于序列的一种
print(max(s3))
print(min(s3))
print(len(s3))

print(9 not in s3)


#删除
del s3
# print(s3)
