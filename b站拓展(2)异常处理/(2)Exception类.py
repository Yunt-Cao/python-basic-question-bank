try:
    num1=int(input())
    num2=int(input())
    print(num1/num2)
except Exception as e:
    print('程序出现异常',e)