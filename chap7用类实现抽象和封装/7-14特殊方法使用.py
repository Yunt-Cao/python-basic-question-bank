#计算
# class Computing:
#     def __init__(self,value):
#         self.value=value
#     def __add__(self, other):
#         lst=[]
#         for i in self.value:
#             lst.append(i+other)
#         return lst
#
#     def __sub__(self, other):
#         lst=[]
#         for i in self.value:
#             lst.append(i-other)
#         return lst
# c=Computing([1,6,9,16])
# print(c+10)
# print(c-2)

#索引和切片
class SelectData:
    def __init__(self,data):
        self.data=data[:]
    def __getitem__(self,index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index]=value
    def __delitem__(self,index):
        del self.data[index]

x=SelectData([1,6,9,16,'ab',False])
print(x)    #x的地址
print(x[:]) #切片，x的全部元素
print(x[2]) #切片，x的第二个元素
print(x[2:]) #从第2个起的全部元素
x[4]=100 #替换第4个元素
print(x[:])
del (x[3])
for num in x:
    print(num,end=' ')