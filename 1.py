import numpy as np

# 全局存储学生姓名、成绩
student_names = []
student_scores = np.array([])

def input_score_data():
    """功能1：录入学生姓名与成绩"""
    global student_names, student_scores
    student_names.clear()
    count = int(input("请输入学生人数："))
    temp_scores = []
    for i in range(count):
        name = input(f"请输入第{i+1}个学生姓名：")
        score = float(input("请输入成绩："))
        student_names.append(name)
        temp_scores.append(score)
    student_scores = np.array(temp_scores)
    print("数据录入完成！\n")

def show_statistics():
    """功能2：成绩统计（均值、最值、中位数、标准差）"""
    if len(student_scores) == 0:
        print("暂无成绩数据，请先录入数据！\n")
        return
    print("==========成绩统计信息==========")
    print(f"总人数：{len(student_scores)}")
    print(f"平均分：{np.mean(student_scores):.2f}")
    print(f"最高分：{np.max(student_scores)}")
    print(f"最低分：{np.min(student_scores)}")
    print(f"中位数：{np.median(student_scores):.2f}")
    print(f"成绩标准差：{np.std(student_scores):.2f}\n")

def show_ranking():
    """功能3：成绩从高到低排名"""
    if len(student_scores) == 0:
        print("暂无成绩数据，请先录入数据！\n")
        return
    # 组合姓名+分数，按分数降序排序
    student_list = list(zip(student_names, student_scores))
    student_list.sort(key=lambda x: x[1], reverse=True)
    print("==========成绩排名（从高到低）==========")
    for idx, (name, score) in enumerate(student_list, start=1):
        print(f"第{idx}名 {name} 分数：{score}")
    print()

def show_distribution():
    """功能4：成绩等级分布划分 优秀>=90 良好80-89 及格60-79 不及格<60"""
    if len(student_scores) == 0:
        print("暂无成绩数据，请先录入数据！\n")
        return
    excellent = student_scores[student_scores >= 90]
    good = student_scores[(student_scores >= 80) & (student_scores < 90)]
    pass_s = student_scores[(student_scores >= 60) & (student_scores < 80)]
    fail = student_scores[student_scores < 60]
    total = len(student_scores)
    print("==========成绩分布统计==========")
    print(f"优秀(90及以上)：{len(excellent)}人，占比{len(excellent)/total*100:.1f}%")
    print(f"良好(80~89)：{len(good)}人，占比{len(good)/total*100:.1f}%")
    print(f"及格(60~79)：{len(pass_s)}人，占比{len(pass_s)/total*100:.1f}%")
    print(f"不及格(60以下)：{len(fail)}人，占比{len(fail)/total*100:.1f}%\n")

def query_student():
    """功能5：根据姓名查询对应成绩"""
    if len(student_scores) == 0:
        print("暂无成绩数据，请先录入数据！\n")
        return
    search_name = input("请输入要查询的学生姓名：")
    if search_name in student_names:
        pos = student_names.index(search_name)
        score = student_scores[pos]
        print(f"学生{search_name}的成绩为：{score}\n")
    else:
        print("未找到该学生！\n")

def show_menu():
    """打印系统主菜单"""
    print("============================\n     成绩分析系统\n============================")
    print("1. 输入成绩数据")
    print("2. 查看成绩统计")
    print("3. 查看成绩排名")
    print("4. 查看成绩分布")
    print("5. 查询学生成绩")
    print("6. 退出系统")

def main():
    while True:
        show_menu()
        select = input("请选择：")
        if select == "1":
            input_score_data()
        elif select == "2":
            show_statistics()
        elif select == "3":
            show_ranking()
        elif select == "4":
            show_distribution()
        elif select == "5":
            query_student()
        elif select == "6":
            print("系统已退出，感谢使用！")
            break
        else:
            print("输入错误，请选择1-6之间的数字！\n")

if __name__ == "__main__":
    main()