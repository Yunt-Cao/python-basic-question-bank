def my_write(s):
    #(1)打开/创建文件
    file = open('b.txt','a',encoding='utf-8')
    #(2)写入内容
    file.write(s)
    file.write('\n')
    #(3)关闭
    file.close()

def my_write_list(file,lst):
    f = open(file,'a',encoding='utf-8')
    f.writelines(lst)
    f.close()

if __name__ == '__main__':
    #my_write('hello')
    #my_write('world')
    lst=['姓名\t','年龄\t','成绩\n','曹云涛\t','18\t','100\t']
    my_write_list('c.txt',lst)