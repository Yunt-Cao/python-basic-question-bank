class Car:
    def __init__(self,type,number):
        self.type=type
        self.number=number

    def start(self):
        print('我是车，我能启动')
    def stop(self):
        print('我是车，我可以停止')


#出租车
class Taxi(Car):
    def __init__(self,type,number,company):
        super().__init__(type,number)
        self.company=company
    # 重写父类的启动和停止方法
    def start(self):
        print('乘客您好')
        print(f'我是{self.company}出租车公司，我的车牌号是：{self.number}，您要去哪里？')

    def stop(self):
        print('目的地到了,请您扫码付款,欢迎下次乘坐')

#家用轿车
class Family(Car):
    def __init__(self,type,number,name):
        super().__init__(type,number)
        self.name = name

    def start(self):
        print(f'我叫{self.name},我的轿车我做主')

    def stop(self):
        print('目的地到了，我们去玩吧!')

#测试
taxi=Taxi('上海大众','京A88888','长城')
taxi.start()
taxi.stop()

print('-'*50)

family=Family('老六','鄂A88888','曹云涛')
family.start()
family.stop()