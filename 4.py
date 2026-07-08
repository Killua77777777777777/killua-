import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("原始数组：")
print(arr)

# 1.取第2行（索引1）第1~3列
part1 = arr[1, 0:3]
print("\n第2行第1~3列：", part1)

# 2.取所有行第3列（下标2）
part2 = arr[:, 2]
print("全部行第3列：", part2)

# 3.步长切片提取第1、3行（下标0、2）
part3 = arr[::2, :]
print("\n奇数行（第1、3行）内容：")
print(part3)

input("\n运行结束，按回车关闭窗口")