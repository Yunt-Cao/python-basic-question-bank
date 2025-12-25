def fib(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fib(i-1)+fib(i-2)
print(fib(9))   #第九位上的数字

for i in range(1,10):
    print(fib(i),end='\t')
print()