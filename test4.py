import matplotlib
import matplotlib.pyplot as plt
import random

# -*- coding: utf-8 -*-

# 设置中文字体 windows和linux
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.rc('font', **font)  # pass in the font dict as kwargs
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simhei.ttf")
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
plt.figure(figsize=(20, 8), dpi=80)
# 绘图
plt.plot(x, y)
# 调整x的刻度
_xtick_lables = ["10点{}分".format(i) for i in range(60)]
_xtick_lables += ["11点{}分".format(i) for i in range(60)]
# 取步长数字和字符串一一对应，数据长度一样 matplotlib默认不显示中文
plt.xticks(list(x)[::3], _xtick_lables[::3], rotation=45, fontpropertues=my_font)

plt.savefig("./t2.png")
if __name__ == '__main__':
    print()
