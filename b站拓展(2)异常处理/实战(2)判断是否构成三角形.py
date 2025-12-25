try:
    a=eval(input('请输入a边的边长:'))
    b=eval(input('请输入b边的边长:'))
    c=eval(input('请输入c边的边长:'))
    if a<0 or b<0 or c<0:
        raise Exception('边长不可为非正数')
    elif a+b<c or c+b<a or a+c<b:
        raise Exception('不满足三角形两边之和大于第三边的原则')
    else:
        print(f'三角形的a,b,c三边长分别为{a},{b},{c}')
except Exception as e:
    print(e)