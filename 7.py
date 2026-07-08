import numpy as np
import timeit

# ========== 任务1：矩阵乘法耗时对比 ==========
setup_code = """
import numpy as np
np.random.seed(12)
A = np.random.rand(1000, 2000)
B = np.random.rand(2000, 3000)
"""
t_dot = timeit.timeit("np.dot(A, B)", setup=setup_code, number=3)
t_at = timeit.timeit("A @ B", setup=setup_code, number=3)
t_matmul = timeit.timeit("np.matmul(A, B)", setup=setup_code, number=3)
print("矩阵乘法平均耗时(执行3次)：")
print(f"np.dot：{t_dot:.3f} s")
print(f"@运算符：{t_at:.3f} s")
print(f"np.matmul：{t_matmul:.3f} s")

# ========== 任务2：C顺序、Fortran顺序内存布局求和测速 ==========
np.random.seed(20)
arr_c = np.random.rand(1000, 1000)  # 默认C行优先存储
arr_f = np.asfortranarray(arr_c.copy()) # F列优先存储

# 按行求和
row_c = timeit.timeit("arr_c.sum(axis=1)", setup="import numpy as np;np.random.seed(20);arr_c=np.random.rand(1000,1000)", number=20)
row_f = timeit.timeit("arr_f.sum(axis=1)", setup="import numpy as np;np.random.seed(20);arr_f=np.asfortranarray(np.random.rand(1000,1000))", number=20)
# 按列求和
col_c = timeit.timeit("arr_c.sum(axis=0)", setup="import numpy as np;np.random.seed(20);arr_c=np.random.rand(1000,1000)", number=20)
col_f = timeit.timeit("arr_f.sum(axis=0)", setup="import numpy as np;np.random.seed(20);arr_f=np.asfortranarray(np.random.rand(1000,1000))", number=20)
print("\n内存布局测速：")
print(f"C布局按行求和耗时：{row_c:.3f} s，F布局按行求和耗时：{row_f:.3f} s")
print(f"C布局按列求和耗时：{col_c:.3f} s，F布局按列求和耗时：{col_f:.3f} s")

# ========== 任务3：复用out参数规避临时数组分配，计算 A²+2A+1 ==========
np.random.seed(30)
A = np.random.rand(500, 500)
res = np.empty_like(A)
# A平方写入res
np.multiply(A, A, out=res)
# 累加2*A
np.add(res, np.multiply(2, A), out=res)
# 累加常数1
np.add(res, 1, out=res)
print("\n表达式A^2 + 2*A + 1运算完成，结果形状：", res.shape)

input("\n运行结束，按回车关闭窗口")