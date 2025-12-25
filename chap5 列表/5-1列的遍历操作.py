lst=['hello','world','python','php']



#for循环遍历列表
for item in lst:
    print(item)



#for range len
for i in range(len(lst)):
    print(i,'--->', lst[i])

#while
i=0
result=[]
while i<len(lst):
    result.append(lst[i])
    i+=1
print(result)

#enumerate函数
for index , item in enumerate(lst):
    print(index,'--->', item)
for index , item in enumerate(lst,start=1):
    print(index,'--->', item)