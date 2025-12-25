lst=[11,895,54,621,145,55,0,-8]
#降序
lst.sort(reverse=True)
print(lst)
# 升序
lst.sort(reverse=False)
print(lst)

lst2=['Banana','apple','Pear','orange']
# 英文降序  先排大写 再排小写  大写的ASCll码比小写的大32
lst2.sort(reverse=True)
print(lst2)
lst2.sort(reverse=False)
print(lst2)


#忽略大小写排序
lst2.sort(key=str.lower)
print(lst2)
lst2.sort(key=str.upper,reverse=True)
print(lst2)