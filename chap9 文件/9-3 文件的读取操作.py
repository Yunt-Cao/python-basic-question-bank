def my_read(filename):
     file=open(filename,'w+',encoding='utf-8')
     file.write('你好啊')
     #写入完成，文件的指针在最后

     #seek,修改文件指针的位置
     file.seek(3)   #3个字节，一个中文占三个字节，utf-8
     #读取
     s=file.read()
     print(type(s),s)

     file.close()

if __name__=='__main__':
    my_read('d.txt')