class Group:
    #类成员，记录班级总分和人数
    total=0
    count=0
    #实例方法,设置单个学生的分数
    def set_score(self,score):
        self.total=score #实例属性，存储单个学生分数
        #调用类方法累计总分人数和
        Group.sum(score)
    #类方法：累计总分人数和
    @classmethod    #表示此为类方法，而非实例方法
    def sum(cls,score):
        cls.total+=score
        cls.count+=1
    #类方法，计算平均分
    @classmethod
    def avg(cls):
        return cls.total/cls.count

#交互式输入学生成绩
group=Group()
while True:
    try:
        score_input=input('请输入学生成绩  （输入end结束）：')
        if score_input=='end':
            break
        score=float(score_input)
        if score<0 or score>100:
            print('成绩应在0~100之间,请重新输入')
            continue
        group.set_score(score)
    except ValueError:
        print('输入无效，请输入数字或end结束')

#显示结果
print(f'班级总分:{group.total}')
print(f'班级人数:{group.count}')
print(f'班级平均数:{group.avg():.2f}')