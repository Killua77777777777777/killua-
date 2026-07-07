import math

# 1.加法函数
def add(a, b):
    return a + b

# 2.减法函数
def sub(a, b):
    return a - b

# 3.乘法函数
def mul(a, b):
    return a * b

# 4.除法函数
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b

# 5.幂运算函数
def power(a, b):
    return a ** b

# 6.平方根开方函数
def sqrt_func(num):
    if num < 0:
        raise ValueError("负数无法开平方")
    return math.sqrt(num)

# 7.保存记录到文件
def save_record(content):
    with open("calc_log.txt", "a", encoding="utf-8") as f:
        f.write(content + "\n")

# 8.读取历史记录
def read_history():
    try:
        with open("calc_log.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        if len(lines) == 0:
            print("暂无任何计算历史记录！")
            return
        print("\n======== 历史计算记录 ========")
        for line in lines:
            print(line.strip())
        print("==============================\n")
    except FileNotFoundError:
        print("暂无记录文件，还没有进行过计算！")

# 计算器运算核心
def calculate():
    print("\n===== 计算器运算面板 =====")
    print("运算指令：+ 加 | - 减 | * 乘 | / 除 | ^ 幂运算 | sqrt 开平方")
    op = input("请输入运算符号：")
    try:
        if op == "sqrt":
            n = float(input("请输入要开方的数字："))
            res = sqrt_func(n)
            record = f"sqrt({n}) = {res:.2f}"
            print("计算结果：", res)
        else:
            num1 = float(input("输入第一个数字："))
            num2 = float(input("输入第二个数字："))
            if op == "+":
                res = add(num1, num2)
                record = f"{num1} + {num2} = {res:.2f}"
            elif op == "-":
                res = sub(num1, num2)
                record = f"{num1} - {num2} = {res:.2f}"
            elif op == "*":
                res = mul(num1, num2)
                record = f"{num1} * {num2} = {res:.2f}"
            elif op == "/":
                res = div(num1, num2)
                record = f"{num1} / {num2} = {res:.2f}"
            elif op == "^":
                res = power(num1, num2)
                record = f"{num1} ^ {num2} = {res:.2f}"
            else:
                print("无效运算符号！")
                return
            print("计算结果：", res)
        save_record(record)
        print("本次计算已存入历史文件！")
    except ValueError as e:
        print(f"输入错误：{e}")
    except ZeroDivisionError as e:
        print(f"计算错误：{e}")
    except Exception as e:
        print(f"未知错误：{e}")

# 主菜单
def main():
    while True:
        print("\n======== 数学计算器系统 ========")
        print("1. 进行数学计算")
        print("2. 查看全部计算历史记录")
        print("3. 退出程序")
        print("=================================")
        choice = input("请输入功能序号(1/2/3)：")
        if choice == "1":
            calculate()
        elif choice == "2":
            read_history()
        elif choice == "3":
            print("程序退出，所有记录保存在 calc_log.txt 文件中")
            break
        else:
            print("输入错误，请选择1、2、3！")

if __name__ == "__main__":
    main()