# 学生成绩管理系统 数据类型与控制结构综合练习
# 列表存储所有学生，每个学生用字典保存信息
student_list = []

def add_student():
    # 录入学生信息
    print("===== 录入新学生信息 =====")
    stu_id = input("请输入学生学号：")
    # 循环查重，防止学号重复
    for stu in student_list:
        if stu["学号"] == stu_id:
            print("该学号已存在，不能重复添加！")
            return
    stu_name = input("请输入学生姓名：")
    math = float(input("请输入数学成绩："))
    english = float(input("请输入英语成绩："))
    python_score = float(input("请输入Python成绩："))
    # 字典保存单个学生数据
    student_dict = {
        "学号": stu_id,
        "姓名": stu_name,
        "成绩": [math, english, python_score]
    }
    student_list.append(student_dict)
    print(f"学生{stu_name}录入完成！")

def search_student():
    # 按学号查询学生
    print("===== 学生成绩查询 =====")
    target_id = input("输入要查询的学号：")
    find = False
    for stu in student_list:
        if stu["学号"] == target_id:
            find = True
            print("------------------------")
            print(f"学号：{stu['学号']}")
            print(f"姓名：{stu['姓名']}")
            score = stu["成绩"]
            print(f"数学：{score[0]} 英语：{score[1]} Python：{score[2]}")
            avg = sum(score) / len(score)
            print(f"个人平均分：{avg:.2f}")
            print("------------------------")
            break
    if not find:
        print("没有找到该学生！")

def score_statistics():
    # 全部学生成绩统计
    if len(student_list) == 0:
        print("暂无学生数据，无法统计！")
        return
    print("===== 全体成绩统计 =====")
    math_all = []
    english_all = []
    python_all = []
    for stu in student_list:
        s = stu["成绩"]
        math_all.append(s[0])
        english_all.append(s[1])
        python_all.append(s[2])
    # 数学统计
    print("数学：平均分{:.2f} 最高分{} 最低分{}".format(sum(math_all)/len(math_all), max(math_all), min(math_all)))
    # 英语统计
    print("英语：平均分{:.2f} 最高分{} 最低分{}".format(sum(english_all)/len(english_all), max(english_all), min(english_all)))
    # Python统计
    print("Python：平均分{:.2f} 最高分{} 最低分{}".format(sum(python_all)/len(python_all), max(python_all), min(python_all)))

# while循环菜单主界面
while True:
    print("\n======== 学生成绩管理系统 ========")
    print("1. 录入学生信息与成绩")
    print("2. 根据学号查询学生成绩")
    print("3. 全体学生成绩统计")
    print("4. 退出系统")
    print("==================================")
    choice = input("请输入功能序号(1-4)：")
    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        score_statistics()
    elif choice == "4":
        print("程序结束，再见！")
        break
    else:
        print("输入错误，请输入数字1/2/3/4！")