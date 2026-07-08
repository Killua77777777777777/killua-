import numpy as np
np.random.seed(20)
# 任务1：生成0~1浮点数组，归一化映射0~100
raw_arr = np.random.rand(10)
arr_min = raw_arr.min()
arr_max = raw_arr.max()
norm_arr = (raw_arr - arr_min) / (arr_max - arr_min) * 100
print("原始0~1随机数组：")
print(np.round(raw_arr, 3))
print("归一化至0~100的数组：")
print(np.round(norm_arr, 2))

# 任务2：累计和、累计最大值
cumulative_sum = np.cumsum(norm_arr)
cumulative_max = np.maximum.accumulate(norm_arr)
print("\n数组累计和：")
print(np.round(cumulative_sum, 2))
print("数组累计最大值：")
print(np.round(cumulative_max, 2))

input("\n运行结束，按回车关闭窗口")