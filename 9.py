import numpy as np

# 1. 创建1维、2维、3维数组
arr_1d = np.array([2, 4, 6, 8, 10])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_3d = np.random.randint(0, 10, size=(2, 3, 4))
print("一维数组：")
print(arr_1d)
print("二维数组：")
print(arr_2d)
print("三维数组，形状", arr_3d.shape)
print(arr_3d)

# 2. 索引与切片
print("\n一维索引取第3个元素：", arr_1d[2])
print("一维切片1到4位：", arr_1d[1:4])
print("二维取第二行第三列：", arr_2d[1, 2])
print("二维前两行所有列：")
print(arr_2d[:2, :])
print("三维第一层全部数据：")
print(arr_3d[0, :, :])

# 3. 形状变换
print("\n原二维数组形状", arr_2d.shape)
reshape_arr = arr_2d.reshape(9, 1)
print("reshape为(9,1)：")
print(reshape_arr)
trans_arr = arr_2d.T
print("二维数组转置：")
print(trans_arr)
flatten_arr = arr_3d.flatten()
print("三维展平一维，长度", len(flatten_arr))

# 4. 矩阵运算函数
def matrix_add(a, b):
    return a + b

def matrix_mul(a, b):
    return a @ b

def matrix_trans(a):
    return a.T

mat_a = np.array([[1, 2], [3, 4]])
mat_b = np.array([[5, 6], [7, 8]])
print("\n矩阵加法：")
print(matrix_add(mat_a, mat_b))
print("矩阵乘法：")
print(matrix_mul(mat_a, mat_b))
print("矩阵转置：")
print(matrix_trans(mat_a))

# 5. 随机数据统计分析
rand_data = np.random.normal(loc=50, scale=10, size=100)
print("\n随机数据统计：")
print("均值：", np.mean(rand_data))
print("最大值：", np.max(rand_data))
print("最小值：", np.min(rand_data))
print("标准差：", np.std(rand_data))
print("中位数：", np.median(rand_data))

input("\n运行结束，按回车关闭窗口")