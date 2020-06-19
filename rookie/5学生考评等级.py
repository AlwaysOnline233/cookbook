# 学生分数考评等级

while True:
    grade = input("请输入成绩：\n")
    if grade == 'ok':
        break

    grade = int(grade)
    if 90 <= grade <= 100:
        print("成绩等级：A")
    elif 80 <= grade < 90:
        print("成绩等级：B")
    elif 70 <= grade < 80:
        print("成绩等级：C")
    elif 60 <= grade < 70:
        print("成绩等级：D")
    elif 0 <= grade < 60:
        print("成绩等级：不及格")
    else:
        print('成绩输入有误')
