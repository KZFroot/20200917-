import matplotlib
import matplotlib.pyplot as plt
import random
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")
y_1 = [1, 0, 1, 1, 1, 2, 3, 3, 2, 3, 3, 3, 1, 1, 0, 1, 2, 3, 1, 2]
y_2 = [2, 1, 2, 1, 2, 0, 0, 1, 2, 2, 2, 1, 1, 2, 3, 4, 5, 1, 2, 3]
x = range(11, 31)
# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y_1, label="自己", color='red')
plt.plot(x, y_2, label="同桌")
# 设置X轴的刻度
_xtick_lable = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_lable, fontproperties=my_font)
plt.yticks(range(0, 9))

# 绘制网络
plt.grid(alpha=0.5)

# 图例
plt.legend(prop=my_font)

if __name__ == '__main__':
    # 展示
    plt.savefig("t3.png")
