d={'hello':10,'world':20,'python':30}
#访问字典当中的元素
#(1)使用d[key]
print(d['hello'])
#(2)d.get(key)
print(d.get('hello'))

# 如果key不存在，d[key]报错     d.get(key)可以指定默认值
print(d.get('java','不存在')) #后面的为设置的默认值
# print(d['java'])


#字典的遍历
for item in d.items():
    print(item)

for key,value in d.items():
    print(key,'--->',value)