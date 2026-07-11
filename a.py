import pandas as pd
import numpy as np

# 1.加载公开数据集（在线拉取，无需手动下载文件）
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
print("====原始数据基础信息====")
print(f"原始行数:{df.shape[0]} 列数:{df.shape[1]}")
print("各列缺失值统计：")
print(df.isnull().sum())
print("重复行数量：", df.duplicated().sum())

# 2.重复记录处理：删除完全重复行
df = df.drop_duplicates(keep="first")

# 3.三类缺失值处理
## 方式1：高缺失率列直接删除（Cabin船舱列缺失占比高，无太多分析价值）
df = df.drop(columns=["Cabin"])
## 方式2：分类变量众数填充（Embarked登船港口）
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
## 方式3：数值列线性插值填充（Age年龄，适合连续时序类缺失修补）
df["Age"] = df["Age"].interpolate(method="linear")

# 4.异常值识别+截断（Age年龄，用四分位IQR规则筛异常）
q1, q3 = df["Age"].quantile([0.25, 0.75])
iqr = q3 - q1
lower_bound, upper_bound = q1 - 1.5*iqr, q3 + 1.5*iqr
df["Age"] = np.clip(df["Age"], lower_bound, upper_bound)

# 5.数据类型标准化
df["Survived"] = df["Survived"].astype("category")
df["Pclass"] = df["Pclass"].astype("category")
df["Name"] = df["Name"].str.strip() #去除文本首尾空格

# 6.清洗结果核验输出
print("\n====清洗后数据校验====")
print("清洗后缺失值统计：")
print(df.isnull().sum())
print(f"清洗完成后数据规模：{df.shape}")
print("数据类型：")
print(df.dtypes)
# 导出清洗完成数据
df.to_csv("titanic_cleaned.csv",index=False,encoding="utf-8-sig")