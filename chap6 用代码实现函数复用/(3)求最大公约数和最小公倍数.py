def gac(m,n):
    while n != 0:
        m,n = n,m%n
    return abs(m)
#利用最大公约数求最小公倍数
def lcm(m,n):
    if n == 0 and m == 0:
        return 0
    return abs(m*n)//gac(m,n)
print(lcm(2,3))
print(gac(2,3))
print(lcm(-8,12))
print(gac(-8,12))