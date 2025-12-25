students=[{'no':'2025001341','name':'cyt','score':'100'},
          {'no':'2025001314','name':'潘雨婷','score':'100'},
          {'no':'2025001344','name':'很开心','score':'85'},]
search_student=input('请输入学生姓名:')
found=None
for student in students:
    if student['name']==search_student:
        found=student
        break
print(found if found else '未找到')
