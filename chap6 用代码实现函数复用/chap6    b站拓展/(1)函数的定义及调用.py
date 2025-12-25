def get_sum(num):
    s=0
    for i in range(1,num+1):
        s+=i
    return print(f'1到{num}的累加和为:{s}')
#函数的调用
get_sum(10)
get_sum(100)#计算1-100的和
