import numpy as np
# 固定随机种子，结果可复现
np.random.seed(10)
# 任务1：逐元素乘法、矩阵乘法
A = np.random.randint(1, 6, size=(2, 3))
B = np.random.randint(1, 6, size=(2, 3))
elem_mult = A * B
mat_mult = A @ B.T
print("数组A：\n", A)
print("数组B：\n", B)
print("逐元素相乘 A * B：\n", elem_mult)
print("矩阵乘法 A @ B.T：\n", mat_mult)

# 任务2：按列、按行求和
sum_mat = np.array([[1, 2], [3, 4]])
col_sum = np.sum(sum_mat, axis=0)
row_sum = np.sum(sum_mat, axis=1)
print("\n按列求和(axis=0)：", col_sum)
print("按行求和(axis=1)：", row_sum)

# 任务3：均值、标准差、四舍五入
float_arr = np.array([1.2, 3.5, 2.8])
avg = np.mean(float_arr)
std = np.std(float_arr)
round_res = np.round(float_arr)
print("\n数组均值：", round(avg, 2))
print("数组标准差：", round(std, 2))
print("四舍五入结果：", round_res)

input("\n运行结束，按回车关闭窗口")