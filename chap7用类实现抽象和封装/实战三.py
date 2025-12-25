class Instrument:
    def make_sound(self):
        pass

class Erhu(Instrument):
    def make_sound(self):
        print('二胡在弹奏')

class Piano(Instrument):
    def make_sound(self):
        print('钢琴在弹奏')

class Violin(Instrument):
    def make_sound(self):
        print('小提琴在弹奏')


#编写一个函数
def play(obj):
    obj.make_sound()

#测试
erhu=Erhu()
piano=Piano()
violin=Violin()

#调用方法
play(erhu)
play(piano)
play(violin)
