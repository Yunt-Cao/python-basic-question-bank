s='hello world'
print('{0:*<20}'.format(s))
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))

#居中对齐
print(s.center(20,'*'))

#千位分隔符(只适用于整数和浮点数)
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.654221))

#小数部分
print('{0:.2f}'.format(3.1415926))

#字符串类型.表示是最大的显示长度
print('{0:.5}'.format('string'))

#整数类型进制转换
a=425
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x}'.format(a))

#浮点数类型
b=3.1415926535
print('保留两位小数{0:.2f},科学计数法：{0:.2e},{0:.2E},百分数：{0:.2%}'.format(b))

#%占位符
name='曹云涛'
age=18
score=98.5
print('姓名:%s,年龄:%d,分数:%f' % (name,age,score))