s='伟大的中国梦'
# 编码 str-->bytes
scode=s.encode(errors='replace')   #默认是utf-8,因为utf-8中文占三个字节 英文一个
print(scode)

scode_gbk=s.encode('gbk',errors='replace')  #gbk中中文占两个字节
print(scode_gbk)

#编码中的出错问题
s2='耶✌'
scode_error=s2.encode('gbk',errors='ignore')    #ignore为出错就会忽略不编了,strick严格的会出错,replace替换成？
print(scode_error)

# s2='耶✌'
# scode_error=s2.encode('gbk',errors='strick')
# print(scode_error)

s2='耶✌'
scode_error=s2.encode('gbk',errors='replace')
print(scode_error)

#解码过程bytes-->str
print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode,'utf-8'))