import math

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*(self.radius**2)

    def perimeter(self):
        return 2*math.pi*self.radius

radius=eval(input('请输入圆的半径：'))
circle=Circle(radius)
# 调用方法
area=circle.area()
perimeter=circle.perimeter()

print(area)
print(perimeter)