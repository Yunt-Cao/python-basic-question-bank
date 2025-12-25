def copy(src,new_path):
    #文件的复制就是边读边写操作
    #(1)打开
    file1=open(src,'rb')
    #(2)打开目标文件
    file2=open(new_path,'wb')
    #(3)开始复制
    s=file1.read()
    file2.write(s) #向目标文件写入所有

    #（关闭）
    file1.close()
    file2.close()   #先打开的后关，后打开的先关

if __name__=='__main__':
    scr='./阿🐎特拉斯.jpg'     #./表示在同一目录
    new_path='../chap8 使用模块和库编程/copy_阿🐎特拉斯.ipg'     #两个..表示上极目录，相当于windows后退
    copy(scr,new_path)
    print('文件复制完毕')