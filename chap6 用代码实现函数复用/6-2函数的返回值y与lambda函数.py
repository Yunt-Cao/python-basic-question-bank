def findwords(sentence):
    result=[]
    for word in sentence.split():
        if word.find('e'or 'E')!=-1:
            result.append(word)
    return result
ss='Return the lowest common ancestor of two words.'
print(findwords(ss))

#lambda函数
import math
area=lambda r:math.pi*r*r
volume=lambda r,h:math.pi*r*r*h
print('{:6.2f}'.format(area(2)))
print(volume(2,3))


lst1=[3,5,-4,-1,0,-2,-6]
lst2= sorted(lst1,key=lambda x:abs(x))
print(lst2)
