#使用()去创造元组
t=('传教','daj',55)
print(t)

#使用tuple()
t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)

print('10在元组中是否存在：',10 in t)
print(max(t))
print(len(t))
print(t.count(10))
print(t.index(40))

#如果元组只有一个元素','不能省
y=(10,)
print(y,type(y))

#元组的删除
del t

# print(t)