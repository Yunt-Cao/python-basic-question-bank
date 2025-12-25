lst1=['read','write','tell','seek']
dict1={'type1':'TextFile','type2':'BinaryFile'}
fileb=open(r'2.dat', 'wb')
#写入数据
import pickle
pickle.dump(lst1,fileb)
pickle.dump(dict1,fileb)
fileb.close()
#读取数据
fileb=open(r'2.dat', 'rb')
fileb.read()
fileb.seek(0)

x=pickle.load(fileb)
y=pickle.load(fileb)
print(x,y)