import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 全局配置解决matplotlib中文乱码、负号显示异常
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ===================== 1、构建抖音精选数据集 =====================
data = {
    "video_id":["v001","v002","v003","v004","v005","v006","v007","v008","v009","v010","v011","v012","v013","v014","v015",
                "v016","v017","v018","v019","v020","v021","v022","v023","v024","v025","v026","v027","v028","v029","v030","v031","v032"],
    "publish_time":[
        "2026-06-01 12:30","2026-06-01 18:10","2026-06-02 09:20",None,"2026-06-02 20:15","2026-06-03 11:00","2026-06-03 19:40",
        "2026-06-04 14:20","2026-06-04 21:10","2026-06-05 08:30","2026-06-05 17:50","2026-06-06 13:10","2026-06-06 22:00",
        "2026-06-07 10:20","2026-06-07 20:30","2026-06-08 11:25","2026-06-08 19:35","2026-06-09 07:40","2026-06-09 22:20",
        "2026-06-10 13:50","2026-06-10 18:45","2026-06-11 10:15","","2026-06-11 21:05","2026-06-12 09:10","2026-06-12 20:00",
        "2026-06-13 12:20","2026-06-13 23:10","2026-06-14 08:55","2026-06-14 17:20","2026-06-15 11:40","2026-06-15 19:50"
    ],
    "category":["美食","美妆","数码","家居","美食","数码","美妆","家居","美食","数码","美妆","家居","美食","数码","美妆",
                "美食","美妆","数码","家居","美食","数码","美妆","家居","美食","数码","美妆","家居","美食","数码","美妆","美食","美妆"],
    "tag":["探店测评","妆容教程","配件开箱","家装改造","菜谱分享","显卡测评","护肤干货","软装避雷","街边小吃","外设测评",
           "口红试色","收纳技巧","夜宵探店","主机评测","粉底测评","烘焙教程","眼影教学","耳机拆解","家具选购","火锅探店",
           "键盘测评","防晒科普","置物架攻略","烧烤测评","屏幕评测","香水分享","灯具挑选","甜品打卡","硬盘测评","气垫测评",
           "茶饮测评","腮红教程"],
    "play_num":[12500,36800,8900,None,42100,15600,51200,9300,48600,17200,63500,10100,52700,18900,71300,39200,44800,11300,13700,
                55100,20400,67900,14200,49800,22100,74200,15300,61400,24700,80600,43300,58200],
    "like_num":[1200,4100,860,120,4600,1520,5800,910,5300,1680,7200,980,5600,1830,8100,4350,5010,1070,1410,6120,2150,7930,
                1540,5740,2390,8710,1680,6970,2680,9520,4820,6640],
    "comment_num":[186,523,95,21,612,210,745,103,689,236,915,116,762,251,1023,541,627,132,179,753,268,987,191,708,297,1104,
                   213,856,334,1217,596,821],
    "share_num":[320,960,152,36,1120,365,1430,172,1280,410,1760,195,1350,443,1920,1015,1162,208,304,1441,487,1796,339,1375,
                 542,2083,371,1604,611,2296,1132,1537],
    "author_type":["普通达人","头部达人","中等达人","普通达人","头部达人","中等达人","头部达人","普通达人","头部达人","中等达人","头部达人",
                    "普通达人","头部达人","中等达人","头部达人","头部达人","头部达人","中等达人","普通达人","头部达人","中等达人","头部达人",
                    "普通达人","头部达人","中等达人","头部达人","普通达人","头部达人","中等达人","头部达人","头部达人","头部达人"],
    "fans_range":["1w-10w","50w以上","10w-50w","1w以内","50w以上","10w-50w","50w以上","1w-10w","50w以上","10w-50w","50w以上","1w以内",
                 "50w以上","10w-50w","50w以上","50w以上","50w以上","10w-50w","1w-10w","50w以上","10w-50w","50w以上","1w以内","50w以上",
                 "10w-50w","50w以上","1w-10w","50w以上","10w-50w","50w以上","50w以上","50w以上"]
}
df = pd.DataFrame(data)

print("====================原始数据概况====================")
print("数据集行数、列数：", df.shape)
print("\n各字段缺失数量：")
print(df.isnull().sum())
print("重复视频条数：", df.duplicated().sum())

# ===================== 2、数据清洗处理 =====================
# 删除完全重复数据
df = df.drop_duplicates(keep="first")

# 删除发布时间为空的样本，时间无法补全
df = df.dropna(subset=["publish_time"])

# 播放量缺失使用线性插值填充
df["play_num"] = df["play_num"].interpolate(method="linear")

# IQR方法处理播放量异常值
q25_play = df["play_num"].quantile(0.25)
q75_play = df["play_num"].quantile(0.75)
iqr_play = q75_play - q25_play
low_play = q25_play - 1.6 * iqr_play
high_play = q75_play + 1.6 * iqr_play
df["play_num"] = np.clip(df["play_num"], low_play, high_play)

# IQR方法处理转发量异常值
q25_share = df["share_num"].quantile(0.25)
q75_share = df["share_num"].quantile(0.75)
iqr_share = q75_share - q25_share
low_share = q25_share - 1.6 * iqr_share
high_share = q75_share + 1.6 * iqr_share
df["share_num"] = np.clip(df["share_num"], low_share, high_share)

# 统一转换时间格式，提取发布小时
df["publish_time"] = pd.to_datetime(df["publish_time"])
df["hour"] = df["publish_time"].dt.hour

# 分类字段转换类型，减少内存占用
df["category"] = df["category"].astype("category")
df["author_type"] = df["author_type"].astype("category")
df["fans_range"] = df["fans_range"].astype("category")

# 计算衍生互动指标
df["like_rate"] = round(df["like_num"] / df["play_num"], 4)
df["comment_rate"] = round(df["comment_num"] / df["play_num"], 4)
df["share_rate"] = round(df["share_num"] / df["play_num"], 4)
df["total_interact"] = df["like_num"] + df["comment_num"] + df["share_num"]

# 划分视频流量等级
level_list = []
for idx, row in df.iterrows():
    play = row["play_num"]
    lr = row["like_rate"]
    if play >= 32000 and lr >= 0.09:
        level_list.append("爆款视频")
    elif play >= 14000:
        level_list.append("潜力视频")
    else:
        level_list.append("普通视频")
df["video_level"] = level_list

print("\n====================清洗后数据校验====================")
print("清洗后缺失值统计：")
print(df.isnull().sum())
print("清洗后数据集大小：", df.shape)
print("\n各流量等级视频数量：")
print(df["video_level"].value_counts())

# 导出清洗完成的数据文件
df.to_csv("douyin_clean.csv", index=False, encoding="utf-8-sig")

# ===================== 3、多维度统计分析 =====================
flow_cols = ["play_num","like_num","comment_num","share_num","like_rate","comment_rate","share_rate","total_interact"]
print("\n====================流量指标描述统计====================")
print(df[flow_cols].describe().round(2))

print("\n====================各品类平均流量====================")
cat_avg = df.groupby("category")[flow_cols].mean().round(2)
print(cat_avg)

print("\n====================各发布时段平均播放量====================")
hour_avg = df.groupby("hour")["play_num"].mean().round(0)
print(hour_avg)

print("\n====================达人类型流量对比====================")
author_avg = df.groupby("author_type")["play_num"].mean().round(0)
print(author_avg)

# 流量指标相关系数矩阵
corr = df[["play_num","like_num","comment_num","share_num","total_interact"]].corr()
print("\n====================流量指标相关系数====================")
print(corr.round(2))

# ===================== 4、可视化绘图 =====================
# 图1 每日平均播放时序折线
daily_data = df.resample("D", on="publish_time")["play_num"].mean()
plt.figure(figsize=(11,4))
daily_data.plot(color="#d62728")
plt.title("每日视频平均播放量变化趋势", fontsize=12)
plt.xlabel("发布日期", fontsize=10)
plt.ylabel("平均播放量", fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("1_每日播放趋势.png", dpi=150)
plt.close()

# 图2 各品类平均播放柱状图
plt.figure(figsize=(8,5))
cat_play = df.groupby("category")["play_num"].mean()
cat_play.plot(kind="bar")
plt.title("不同内容品类平均播放量对比", fontsize=12)
plt.xlabel("视频内容品类", fontsize=10)
plt.ylabel("平均播放量", fontsize=10)
plt.tight_layout()
plt.savefig("2_品类播放对比.png", dpi=150)
plt.close()

# 图3 各时段播放量柱状图
plt.figure(figsize=(9,4))
hour_avg.plot(kind="bar", color="#4b89dc")
plt.title("各发布时段平均播放量分布", fontsize=12)
plt.xlabel("发布小时", fontsize=10)
plt.ylabel("平均播放量", fontsize=10)
plt.tight_layout()
plt.savefig("3_时段流量分布.png", dpi=150)
plt.close()

# 图4 播放量与点赞散点图
plt.figure(figsize=(7,5))
sns.scatterplot(x="play_num", y="like_num", data=df, alpha=0.6)
plt.title("视频播放量与点赞量分布关系", fontsize=12)
plt.xlabel("播放量", fontsize=10)
plt.ylabel("点赞数量", fontsize=10)
plt.tight_layout()
plt.savefig("4_播放点赞散点.png", dpi=150)
plt.close()

# 图5 流量等级数量饼图
plt.figure(figsize=(6,6))
level_count = df["video_level"].value_counts()
plt.pie(level_count, labels=level_count.index, autopct="%.1f%%")
plt.title("视频流量等级占比分布", fontsize=12)
plt.tight_layout()
plt.savefig("5_流量等级饼图.png", dpi=150)
plt.close()

# 图6 相关性热力图
plt.figure(figsize=(7,5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("流量指标相关性热力图", fontsize=12)
plt.tight_layout()
plt.savefig("6_指标相关性热力图.png", dpi=150)
plt.close()

# ===================== 5、业务分析总结 =====================
best_cat = cat_avg["play_num"].idxmax()
best_h = hour_avg.idxmax()
best_author = author_avg.idxmax()

print("\n====================业务分析总结====================")
print(f"1、流量表现最好的内容品类：{best_cat}，平均播放量 {cat_avg.loc[best_cat, 'play_num']:.0f}")
print(f"2、播放效果最优发布时段：{best_h}点")
print(f"3、流量最高达人类型：{best_author}")
print("4、运营建议：优先产出美妆、美食类内容，晚间高流量时段发布；播放量与互动数据高度正相关，高播放视频互动表现更好。")
print("\n所有清洗数据。")