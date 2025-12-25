class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getDiscriminant(self):
        return self.b**2 - 4*self.a*self.c
    def getRoot1(self):
        delta = self.getDiscriminant()
        if delta < 0:
            return 0
        return (-self.b + delta**0.5) / (2*self.a)
    def getRoot2(self):
        delta = self.getDiscriminant()
        if delta < 0:
            return 0
        return (-self.b - delta**0.5) / (2*self.a)
    def getRoots(self):
        return self.getRoot1(), self.getRoot2()


#测试方程
eq1 = Equation(1,0,1)
print(f'方程：{eq1.a}x²+{eq1.b}x+{eq1.c}=0')
print(f'判别式={eq1.getDiscriminant()}')
print(f'根1={eq1.getRoot1()}')
print(f'根2={eq1.getRoot2()}')
print(f'所有根={eq1.getRoots()}')
print()
eq2 = Equation(1,-3,2)
print(f'方程：{eq2.a}x²+{eq2.b}x+{eq2.c}=0')
print(f'判别式={eq2.getDiscriminant()}')
print(f'根1={eq2.getRoot1()}')
print(f'根2={eq2.getRoot2()}')
print(f'所有根={eq2.getRoots()}')