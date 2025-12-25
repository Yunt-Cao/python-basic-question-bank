input_str=input('请输入用逗号隔开的元素：'.split(','))
new_lst=[]
for word in input_str:
    if word not in new_lst:
        new_lst.append(word)
print(new_lst)