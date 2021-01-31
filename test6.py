import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 散点图绘制
y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
       22, 23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12, 13, 6]
x_3 = range(1, 32)
x_10 = range(51, 82)

# 设置图形大小
plt.figure(figsize = (20, 8), dpi=80)
plt.scatter(x, y_3)

if __name__ == '__main__':
    # 展示
    plt.show()
