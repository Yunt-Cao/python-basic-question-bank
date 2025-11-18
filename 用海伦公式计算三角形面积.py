import math
try:
    a=eval(input('请输入a边的边长：'))
    b=eval(input('请输入b边的边长：'))
    c=eval(input('请输入c边的边长：'))
except NameError:
    print('请输入正确的边长')
if a<0 or b<0 or c<0:
    print('三角形边长不应为负数')
elif a+b<c or b+c<a or a+c<b:
    print('不符合三角形两边之和大于第三边：')
else:
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('三角形的面面积是：{:.2f}'.format(s),'p的值是：{:.2f}'.format(p))