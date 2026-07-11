import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["font.sans-serif"] = ["SimHei"] #解决中文乱码
plt.rcParams["axes.unicode_minus"] = False

# 1.读取UCI北京PM2.5数据集
url = "https://raw.githubusercontent.com/sutin1234/Beijing-PM2.5/master/PRSA_Data_20130301-20170228.csv"
df = pd.read_csv(url)
# 拼接规范日期列
df["date"] = pd.to_datetime(df[["year","month","day","hour"]])
df = df.set_index("date")

# 2.基础预处理：剔除空值
df = df.dropna(subset=["PM2.5","PM10","SO2","NO2","CO","O3"])

# 3.污染物基础统计指标
pollutant_cols = ["PM2.5","PM10","SO2","NO2","CO","O3"]
desc_stats = df[pollutant_cols].describe().round(2)
print("====污染物描述性统计====")
print(desc_stats)
corr_matrix = df[pollutant_cols].corr()
print("\n====污染物相关系数矩阵====")
print(corr_matrix.round(2))

# 4.多类图表绘制
## 图1：月度PM2.5均值折线图（时序季节性规律）
month_pm = df["PM2.5"].resample("M").mean()
plt.figure(figsize=(12,4))
month_pm.plot(color="#d62728")
plt.title("月度PM2.5平均浓度时序变化")
plt.xlabel("日期")
plt.ylabel("PM2.5 μg/m³")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("1_pm_month_trend.png",dpi=200)
plt.close()

## 图2：各污染物季度均值柱状图
df["quarter"] = df.index.quarter
quarter_avg = df.groupby("quarter")[pollutant_cols].mean()
quarter_avg.plot(kind="bar",figsize=(10,5))
plt.title("分季度各类污染物平均浓度")
plt.xlabel("季度")
plt.ylabel("污染物浓度")
plt.legend(bbox_to_anchor=(1.02, 1))
plt.tight_layout()
plt.savefig("2_quarter_bar.png",dpi=200)
plt.close()

## 图3：PM2.5-PM10散点图（相关性直观展示）
plt.figure(figsize=(7,5))
sns.scatterplot(x=df["PM2.5"],y=df["PM10"],alpha=0.2,s=12)
plt.title("PM2.5与PM10浓度散点分布")
plt.tight_layout()
plt.savefig("3_scatter_pm.png",dpi=200)
plt.close()

## 图4：污染物相关性热力图
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix,annot=True,fmt=".2f",cmap="RdYlGn_r")
plt.title("污染物相关性热力图")
plt.tight_layout()
plt.savefig("4_corr_heatmap.png",dpi=200)
plt.close()

# 季节性业务结论输出
season_pm = df.groupby("quarter")["PM2.5"].mean().sort_values(ascending=False)
print("\n分季度PM2.5均值（判断季节规律）：")
print(season_pm)
print("业务解读：冬季（Q4、Q1）供暖叠加静风天气，PM2.5污染水平显著高于春夏季度")