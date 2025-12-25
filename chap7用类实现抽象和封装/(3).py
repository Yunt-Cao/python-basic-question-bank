class FreeFall:
    def __init__(self,h0,v0=0,g=9.8):
        self.h0 = h0
        self.v0 = v0
        self.g = g

    def velocity(self,t):
        return self.v0 + self.g*t
    def displacement(self,t):
        return 0.5 * self.g * t**2

#测试
fall=FreeFall(100)
print(f't=2s:速度={fall.velocity(2):.1f}m/s,位移={fall.displacement(2):.1f}m')
