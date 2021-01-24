import numpy as np
import matplotlib.pyplot as plt

# subplots创建多个子图
x = np.arange(0, 100)
# 划分子图
fig, axes = plt.subplots(2, 2)
ax1 = axes[0, 0]
ax2 = axes[0, 1]
ax3 = axes[1, 0]
ax4 = axes[1, 1]
# 作图1
ax1.plot(x, x)
# 作图2
ax2.plot(x, -x)
# 作图3
ax3.plot(x, x ** 2)
ax3.grid(color='r', linestyle='--', linewidth=1, alpha=0.3)
# 作图4
ax4.plot(x, np.log(x))

# 面向对象API：add_subplots与add_axes新增子图或区域
# add_subplot与add_axes都是面对象figure编程的，pyplot api中没有此命令
# 1 add_subplot的参数与subplots的相似
x = np.arange(0, 100)
# 新建figure对象
fig = plt.figure()
# 新建子图1
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x, x)
# 新建子图3
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(x, x ** 2)
ax3.grid(color='r', linestyle='--', linewidth=1, alpha=0.3)
# 新建子图4
ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(x, np.log(x))

# 新建图中图
# 新建figure
fig = plt.figure()
# 定义数据
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]
# 新建区域ax1
#figure的百分比,从figure 10%的位置开始绘制, 宽高是figure的80%
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_title('area1')
#新增区域ax2,嵌套在ax1内
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x,y, 'b')
ax2.set_title('area2')
if __name__ == '__main__':
    plt.show()
