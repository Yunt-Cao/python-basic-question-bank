try:
    num1=int(input('请输入一个整数:'))
    num2=int(input('请输入另一个整数:'))
    result=num1/num2
except ZeroDivisionError:
    print('分母不可为0')
except ValueError:
    print('请输入阿拉伯数字')
else:   #出错时将不会执行
    print('结果:',result)
finally:
    print('程序运行结束')