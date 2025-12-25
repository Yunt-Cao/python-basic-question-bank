t=('python','hello','world')
print(t[0])
t2=t[0:3:2]
print(t2)


#元素的遍历
for item in t:
    print(item)

for i in range(0,len(t)):
    print(i,t[i])


#使用函数enumerate()
for index,item in enumerate(t,start=100):
    print(index,'--->',item)
    