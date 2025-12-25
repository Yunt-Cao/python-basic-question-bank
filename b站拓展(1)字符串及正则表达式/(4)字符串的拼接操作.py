s1='hello'
s2='world'
#(1)使用+
print(s1+s2)

#(2)使用字符串中的join()
print(''.join([s1,s2]))

print('*'.join(['hello','world','python']))

#(3)直接拼接
print('hello''world')

#(4)使用格式化字符串进行拼接
print('%s%s' % (s1,s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))
