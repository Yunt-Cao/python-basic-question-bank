t=(i for i in range(1,4))
# t=tuple(t)
# print(t)

#遍历
# for index,item in enumerate(t,start=100):
#     print(index,'--->',item)

print(t.__next__())
print(t.__next__())
print(t.__next__())

t=tuple(t)
print(t)