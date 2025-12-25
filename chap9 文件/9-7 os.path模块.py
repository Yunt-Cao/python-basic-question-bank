import os.path
#(1)返回path绝对路径
print(os.path.abspath('./阿🐎特拉斯.jpg'))
#（2）返回path的目录
print(os.path.dirname('F:\\python\\chap9 文件\\阿🐎特拉斯.jpg'))
#(3)判断存在
print(os.path.exists('F:\\python\\chap9 文件\\9-6 文件的复制.py'))
#（4）返回path所指向的文件或者目录的最后存储时间
print(os.path.getatime('F:\\python\\chap9 文件\\9-6 文件的复制.py'))
#(5)返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime('F:\\python\\chap9 文件\\9-6 文件的复制.py'))
#（6）返回path文件的（字节）大小
print(os.path.getsize('F:\\python\\chap9 文件\\9-6 文件的复制.py'))
#判断
print(os.path.isabs('F:\\python\\chap9 文件\\9-6 文件的复制.py'))  #绝对路径
print(os.path.isdir('F:\\python\\chap9 文件\\9-6 文件的复制.py'))  #存在的目录
print(os.path.isfile('F:\\python\\chap9 文件\\9-6 文件的复制.py')) #存在文件
#（7）分割目录和文件名
print(os.path.split('F:\\python\\chap9 文件\\9-6 文件的复制.py'))
#(8)分离文件和拓展名
print(os.path.splitext('F:\\python\\chap9 文件\\9-6 文件的复制.py'))