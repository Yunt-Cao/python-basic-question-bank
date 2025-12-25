try:
    score=eval(input('请输入您的成绩:'))
    if score<0 or score>100:
        raise Exception('输入的分数必须在0-100之间')
    else:
        print(f'您的成绩为:{score:.2f}')
except Exception as e:
    print(e)