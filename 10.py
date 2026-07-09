import numpy as np
import matplotlib.pyplot as plt

# 1. 生成模拟股票价格数据
np.random.seed(66)
trading_days = 200
# 生成随机日收益率
daily_return = np.random.normal(loc=0.0008, scale=0.018, size=trading_days)
# 生成股价，初始价格100
price_list = [100]
for r in daily_return:
    new_price = price_list[-1] * (1 + r)
    price_list.append(new_price)
prices = np.array(price_list)

# 2. 计算对数收益率、波动率
log_returns = np.log(prices[1:] / prices[:-1])
annual_volatility = np.std(log_returns) * np.sqrt(252)
print("年化波动率：", round(annual_volatility, 4))

# 3. 计算5日、20日移动平均线
window5 = 5
window20 = 20
ma5 = np.convolve(prices, np.ones(window5)/window5, mode="valid")
ma20 = np.convolve(prices, np.ones(window20)/window20, mode="valid")

# 4. 投资组合风险分析（3只股票）
stock1 = prices
stock2 = prices * np.random.normal(1, 0.02, size=len(prices))
stock3 = prices * np.random.normal(1, 0.03, size=len(prices))
port_data = np.vstack([stock1, stock2, stock3])
port_return = np.diff(np.log(port_data))
cov_matrix = np.cov(port_return)
var_list = np.var(port_return, axis=1)
print("单只股票收益率方差：", np.round(var_list, 6))
print("资产协方差矩阵：")
print(np.round(cov_matrix, 6))

# 5. 可视化绘图
plt.figure(figsize=(12, 6))
plt.plot(prices, label="Stock Price", color="#2277bb")
plt.plot(np.arange(window5-1, len(prices)), ma5, label="MA5", color="#ee7722")
plt.plot(np.arange(window20-1, len(prices)), ma20, label="MA20", color="#22aa44")
plt.title("Simulated Stock Price & Moving Average")
plt.xlabel("Trading Day")
plt.ylabel("Price")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

input("\n运行结束，按回车关闭窗口")