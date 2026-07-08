import numpy as np

# 1. 创建3行4列、0~9随机整数数组
arr = np.random.randint(0, 10, size=(3, 4))
print("原始3行4列数组：")
print(arr)

# 2. 重塑为(4,3)再转置
reshaped_arr = arr.reshape(4, 3).T
print("\n重塑并转置后的数组：")
print(reshaped_arr)

# 3. 提取所有大于5的元素
filtered_arr = arr[arr > 5]
print("\n大于5的所有元素：")
print(filtered_arr)

# 防止窗口直接闪退
input("\n运行结束，按回车关闭窗口")