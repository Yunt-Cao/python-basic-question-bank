'''
str.isdigit()   十进制的阿拉伯数字
str.isnumeric()     数字
str.isalpha()   所有字符都是字母(包含中文字符)
str.isalnum()   所有字符都是数字或字母(包含中文字符)
str.islower()   小写
str.isupper()   大写
str.istitle()   所有字符都是首字母大写
str.isspace()   所有字符都是空白字符(\n,\t等)
'''

print('123'.isdigit())
print('0b1101'.isdigit())
print('-'*50)

print('一二三'.isnumeric())
print('壹贰'.isnumeric())
print('Ⅲ'.isnumeric())
print('-'*50)

print('hello 你好123'.isalpha())
print('hello 你还一二三'.isalpha())
print('-'*50)

print('None'.isspace())
print(' '.isspace())