import numpy as np
np.random.seed(40)
# ========== 任务1：计算对数收益率 ==========
prices = np.array([100, 102, 105, 103, 107])
log_return = np.log(prices[1:] / prices[:-1])
print("每日对数收益率：\n", np.round(log_return, 4))

# ========== 任务2：移动平均线MA5、MA20 ==========
stock_price = np.random.normal(loc=100, scale=3, size=100).cumsum() + 100
window_5, window_20 = 5, 20
ma5 = np.convolve(stock_price, np.ones(window_5)/window_5, mode="valid")
ma20 = np.convolve(stock_price, np.ones(window_20)/window_20, mode="valid")
print("\n5日均线前5个数值：", np.round(ma5[:5], 2))
print("20日均线前5个数值：", np.round(ma20[:5], 2))

# ========== 任务3：波动率、相关系数矩阵 ==========
daily_return = np.random.normal(loc=0.0005, scale=0.02, size=(1000, 252))
annual_vol = daily_return.std(axis=1) * np.sqrt(252)
corr_matrix = np.corrcoef(daily_return)
print("\n前5只股票年化波动率：", np.round(annual_vol[:5], 4))
print("相关系数矩阵形状：", corr_matrix.shape)

input("\n运行结束，按回车关闭窗口")