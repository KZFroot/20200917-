from pandas import np
import pandas as pd
import matplotlib.pyplot as plt  # matplotlib图形展示库

if __name__ == '__main__':
    for i in range(1, 3):
        print(i)
# 等差数列
# print(np.linspace(1, 10, 9))
# list函数
var = ['h', 'e', '1', '1', 'o']
# print(var[1:3])

# 数据训练
df =pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9],
    'D': [1, 3, 5],
    'E': [5, 3, 6],
    'F': [7, 4, 3]
})
# 除了最后一列的所有数据
print(df.iloc[:, :-1])
# 获取最后一列数据
print(df.iloc[:, -1])
# 获取第一列
print(df.iloc[:, 0])
# 获取inex下标为1的数据
print(df.iloc[:, 1])

# 创建画布
# num:图像编号或名称，数字为编号 ，字符串为名称
# figsize:指定figure的宽和高，单位为英寸；
# dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80      1英寸等于2.5cm,A4纸是 21*30cm的纸张
# facecolor:背景颜色
# edgecolor:边框颜色
# frameon:是否显示边框
# figure = plt.figure(num='gg', figsize=(5, 3), dpi=None, facecolor='red', edgecolor=None, frameon=True)
# plt.show()

# 创建单个子图
# nrows:subplot的行数
# ncols:subplot的列数
# sharex：所有subplot应该使用相同的X轴刻度(调节xlim将会影响所有的subplot)
# sharex：所有subplot应该使用相同的Y轴刻度(调节ylim将会影响所有的subplot)
# subpolt_kw:用于创建各subplot的关键字字典
# **fig_kw 创建figure时的其他关键字
# plt.subplot(nrows, ncols, sharex, sharey, subplot_kw, **fig_kw)
x = np.arange(0,100)
# 第一行左图
#作图1
plt.subplot(221)
plt.plot(x, x)
#作图2
plt.subplot(222)
plt.plot(x, -x)
#作图3
plt.subplot(223)
plt.plot(x, x ** 2)
plt.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
#作图4
plt.subplot(224)
plt.plot(x, np.log(x))
plt.show()


