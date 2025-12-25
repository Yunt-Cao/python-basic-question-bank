x=int(input())
def isodd(x):
    if x!=int(x):
        print('请输入整数')
        return
    x=int(x)
    return x%2==1
print(isodd(x))
