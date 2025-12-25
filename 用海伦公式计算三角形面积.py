import math
try:
    a=eval(input('请输入a边长：'))
    b=eval(input('请输入b边长：'))
    c=eval(input('请输入c边长：'))
except NameError:
    print('请输入正数数值')
if a<0 or b<0 or c<0:
    print('三角形的边长应>0')
elif a+b<c or a+c<b or b+c<a:
    print('不符合三角形两边之和大于第三边的原理')
else:
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f'三角形的面积为{s:.2f}')