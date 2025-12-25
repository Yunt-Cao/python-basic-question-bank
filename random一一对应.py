import random
places=['厕所','阳台','洗手台','过道']
people=['曹云涛','丁进辉','陈翔','周鑫']
#随机打乱地点列表
random.shuffle(places)
#zip(people,places)将两个列表按索引一一绑定
for person,place in zip(people,places):
    print(f'{person}在自己值日期间主要打扫:{place}')