#(1)
import re
pattern='黑客|破解|反爬'
s='我想学习Python，像破解一些Vip视频，Python可以实现无底线反爬吗？'
new_s=re.sub(pattern,'XXX',s)
print(new_s)



s2='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=cyt&fenlei=256'
pattern2='[?|&]'
lst=re.split(pattern2,s2)
print(lst)