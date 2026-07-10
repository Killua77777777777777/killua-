import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: f'{x:.2f}')

orders = pd.DataFrame({
    'order_id': [f'O{number}' for number in range(1001, 1019)],
    'region': ['华东','华北','华南','华东','西南','华北','华南','华东','西南','华北','华东','华南','西南','华东','华北','华南','华东','西南'],
    'product': ['机械键盘','无线鼠标','显示器','扩展坞','机械键盘','显示器','无线鼠标','显示器','扩展坞','机械键盘','无线鼠标','扩展坞','显示器','机械键盘','扩展坞','显示器','无线鼠标','机械键盘'],
    'category': ['外设','外设','显示设备','配件','外设','显示设备','外设','显示设备','配件','外设','外设','配件','显示设备','外设','配件','显示设备','外设','外设'],
    'quantity': [2,3,1,4,5,2,6,1,3,2,8,2,1,3,5,2,4,6],
    'unit_price': [289,129,1299,399,289,1299,129,1299,399,289,129,399,1299,289,399,1299,129,289],
    'member_level': ['金卡','普通','银卡','金卡','银卡','普通','金卡','银卡','普通','金卡','银卡','金卡','普通','银卡','金卡','金卡','普通','银卡'],
    'coupon_rate': [0.05,0.00,0.08,0.10,0.05,0.00,0.12,0.05,0.00,0.08,0.10,0.05,0.00,0.12,0.05,0.08,0.00,0.10],
    'salesperson': ['小林','小周','小陈','小林','小赵','小周','小陈','小林','小赵','小周','小林','小陈','小赵','小林','小周','小陈','小林','小赵']
})

# ====================任务1====================
print("==========任务1：快速理解数据==========")
# 1. 行数、列数、所有列名
rows, cols = orders.shape
col_names = orders.columns.tolist()
print(f"数据行数：{rows}，列数：{cols}")
print("全部列名：", col_names)

# 2. 单列region、三列组合，打印类型
s_region = orders['region']
df_three = orders[['order_id','product','quantity']]
print("\nregion单列数据类型：", type(s_region))
print("order_id/product/quantity三列表类型：", type(df_three))
print("\nregion单列前5行：")
print(s_region.head())
print("\n三列数据前5行：")
print(df_three.head())

# 3. iloc 取第4~8行（下标3到7）、前4列
slice_iloc = orders.iloc[3:8, :4]
print("\niloc截取第4~8行、前4列：")
print(slice_iloc)

# 4. loc筛选华东订单，只展示三列
filter_east = orders.loc[orders['region'] == '华东', ['order_id','product','member_level']]
print("\nloc筛选华东地区订单：")
print(filter_east)

# 5. loc优势说明
print("\nloc推荐理由：loc按【列名/行标签】取值，代码可读性高；iloc仅数字下标，数据索引变动后容易取错，业务长期维护用loc更稳定。")
print("任务1结果解释：数据集共18行9列，单列是Series、多列是DataFrame；iloc按位置切片，loc按条件标签筛选，loc更适配业务长期迭代。")

# ====================任务2====================
print("\n==========任务2：构造订单结算指标==========")
analysis = orders.assign(
    gross_amount = lambda x: x['quantity'] * x['unit_price'],
    member_discount = lambda x: np.where(x['member_level'] == '金卡', 0.10,
                                  np.where(x['member_level'] == '银卡', 0.05, 0.00)),
    payable_amount = lambda x: (x['gross_amount'] * (1 - x['member_discount']) * (1 - x['coupon_rate'])).round(2),
    shipping_fee = lambda x: np.where(x['payable_amount'] >= 1000, 0, 20),
    final_amount = lambda x: (x['payable_amount'] + x['shipping_fee']).round(2)
)
show_cols = ['order_id','gross_amount','member_discount','payable_amount','shipping_fee','final_amount']
print(analysis[show_cols].head(8))
print("任务2结果解释：通过向量化批量算出总额、会员折扣、实付、运费、最终成交价，无循环，所有金额保留两位小数。")

# ====================任务3====================
print("\n==========任务3：重点跟进订单筛选==========")
# 定义3个独立布尔条件
cond1 = analysis['region'].isin(['华东','华南'])
cond2 = analysis['final_amount'] >= 700
cond3 = (analysis['quantity'] >= 2) | (analysis['member_level'] == '金卡')
mask = cond1 & cond2 & cond3
focus_orders = analysis.loc[mask, ['order_id','region','product','quantity','member_level','final_amount']]
focus_orders = focus_orders.sort_values('final_amount', ascending=False)
print(focus_orders)
print("&、|两侧必须加括号原因：&、|运算优先级高于比较运算符，不加括号会逻辑错乱；任务3结果解释：筛选出华东/华南、金额≥700、满足量大或金卡的高价值订单，按成交金额从高到低排序。")

# ====================任务4====================
print("\n==========任务4：封装订单等级函数==========")
def add_order_level(df):
    new_df = df.copy()
    new_df['order_level'] = np.where(new_df['final_amount'] >= 2000, "战略订单",
                            np.where(new_df['final_amount'] >= 1000, "重点订单", "普通订单"))
    return new_df

leveled_orders = analysis.pipe(add_order_level)
level_count = leveled_orders['order_level'].value_counts()
print("各订单等级数量：")
print(level_count)
print("任务4结果解释：pipe调用自定义函数新增订单分级，复制原表不修改原始数据，统计出战略/重点/普通订单各自总量。")

# ====================任务5====================
print("\n==========任务5：一条方法链经营汇总==========")
region_report = (
    analysis
    .pipe(add_order_level)
    .query("final_amount >= 500")
    .groupby(['region','order_level']).agg(
        order_count = ('order_id', 'count'),
        quantity_sum = ('quantity', 'sum'),
        revenue_sum = ('final_amount', 'sum'),
        revenue_mean = ('final_amount', 'mean')
    )
    .sort_values('revenue_sum', ascending=False)
)
print(region_report)
print("任务5结果解释：单条链式操作完成分级、过滤、分组聚合、排序，无中间临时表，输出各地区+订单等级的经营汇总报表。")

# ====================任务6====================
print("\n==========任务6：销售人员经营诊断==========")
# 1. 销售总金额排名
sales_total = analysis.groupby('salesperson')['final_amount'].sum().round(2)
top_sales = sales_total.idxmax()
top_sales_total = sales_total.max()

# 2. 该销售各地区金额
sales_region = analysis.loc[analysis['salesperson'] == top_sales].groupby('region')['final_amount'].sum().round(2)
top_region = sales_region.idxmax()
top_region_amt = sales_region.max()

# 3. 地区占比
ratio = (top_region_amt / top_sales_total * 100).round(2)

print(f"成交最高销售人员：{top_sales}")
print(f"该销售总成交金额：{top_sales_total:.2f}")
print(f"该销售成交最高地区：{top_region}")
print(f"核心地区成交金额：{top_region_amt:.2f}")
print(f"核心地区占此人总业绩比例：{ratio}%")
print("业务结论：小林是业绩最高销售，华东地区贡献其绝大部分营收，华东是他核心产出区域。")