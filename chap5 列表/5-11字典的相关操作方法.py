d={1001:'李梅',1002:'王华',1003:'张锋'}
print(d)

#向字典中添加元素
d[1004]='cao yun tao'
print(d)

#获取字典中所以的key
keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

#获取value
values=d.values()
print(list(values))
print(tuple(values))

#如何将字典中的数据转成key-value的形式，以元组的方式进行展示
lst=list(d.values())
print(lst)

#使用pop函数
print(d.pop(1001))
print(d)

print(d.pop(1008,'不存在'))


#popitem
print(d.popitem())
print(d)

d.clear()
print(d)

print(bool(d))
