import matplotlib.pyplot as plt
from pandas import np

fig = plt.figure(figsize=(20, 8), dpi=80)
x = np.arange(2, 26, 2)
# 数据在x轴的位置，是一个可以迭代的对象
y = [15, 13, 14, 5, 17, 20, 25, 26, 26, 17, 22, 1]
# 数据在y轴的位置，是一个可以迭代的对象
# 绘图
plt.plot(x, y)
# 绘制x轴的刻度
plt.xticks(range(2, 25))
# 保存
plt.savefig("./t1.png")
if __name__ == '__main__':
    print(1)


