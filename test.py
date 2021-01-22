from pandas import np
import pandas as pd

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
