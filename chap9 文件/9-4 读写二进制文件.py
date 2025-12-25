fileb=open('1.txt','wb')
fileb.write(b'Hello Python')
n=123
fileb.write(bytes(str(n),encoding='utf-8'))
fileb.write(b'\n3.14')
fileb.close()

#以‘rb’方式打开二进制文件
file=open('1.txt','rb')
print(file.read())
file.close()

print('---'*50)

#'r'
filec=open('1.txt','r')
print(filec.read())
filec.close()