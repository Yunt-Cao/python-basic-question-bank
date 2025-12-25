import random
all_chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E',
           'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           '0','1','2','3','4','5','6','7','8','9']
#用来储存生成的验证码
code=[]
#循环四次 每次不一样
for _ in range(4):
    #随机选一个字符
    char=random.choice(all_chars)
    #把所选的字符加入验证码
    code.append(char)
    #删掉这个字符 避免重复
    all_chars.remove(char)
#把列表变成字符串
x=''.join(code)
print(f'验证码为：{x}')