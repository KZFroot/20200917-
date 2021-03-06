#  实际值和预测值的比较
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # matplotlib图形展示库

# 数据导入
# 一级能开业务量数据、统一接口平台业务量，统一支付_支付业务量，
f1 = open('一级能开业务量.csv')
f2 = open('统一接口平台业务量.csv')
f3 = open('统一支付_在线扣费业务.csv')
f4 = open('统一支付_支付业务.csv')
f5 = open('一级能开业务量.csv')
data1 = pd.read_csv(f1)
data2 = pd.read_csv(f2)
data3 = pd.read_csv(f3)
data4 = pd.read_csv(f4)
data6 = pd.read_csv(f5)
data5 = pd.read_excel('PBOSS.xlsx')


# 设置预测值，根据
# 1.2倍四分位方差，计算异常值
# 根据10天的
def Warningfun(s_q, p=1.2):
    # 计算上下四分位数
    Q1 = s_q.quantile(q=0.25)
    Q3 = s_q.quantile(q=0.75)
    # 异常值判断标准， 1.2倍的四分位差 计算上下须对应的值
    low_quantile = Q1 - p * (Q3 - Q1)
    high_quantile = Q3 + p * (Q3 - Q1)
    # 输出异常值
    return low_quantile, high_quantile


# 获取同比数据
# 2、序列数据抽取（获取同比数据）get_inv_t_data(s_q,inv_t = 48)
# 输入：s_q（数据序列），inv_t:多长间隔取一个数（默认48）
# s_q_len = len(s_q)
# s_q_temp = s_q[np.linspace(0, s_q_len - 1, num=int(s_q_len  / inv_t) + 1, dtype=int)]
# 输出：s_q_temp
def Warningfun_main(s_q, inv_t=48):
    # s_len  = len(series)
    s_q_len = len(s_q)
    # inv_t = 24 * 2
    day_num = 10 * inv_t
    # end_tage = s_len-inv_t
    # result_low = list(series[0:day_num])
    # 截取数据
    result_low = list(s_q[0:day_num])
    # result_high = list(series[0:day_num])
    result_high = list(s_q[0:day_num])
    for index in range(day_num, s_q_len):
        # index = 959
        # series_temp = series[(index - day_num):index].reset_index(drop=True)
        s_q_temp = s_q[(index - day_num):index].reset_index(drop=True)
        # index_flage = np.linspace(0, day_num, num=int(day_num / inv_t) + 1, dtype=int)
        # series_temp2 = series_temp[np.linspace(0, day_num - 1, num=int(day_num / inv_t) + 1, dtype=int)]  # 获取同比数据
        # 等差数列 获取同比数据
        s_q_temp2 = s_q_temp[np.linspace(0, day_num - 1, num=int(day_num / inv_t) + 1, dtype=int)]  # 获取同比数据
        # 获取四分位 异常值
        low_quantile, high_quantile = Warningfun(s_q_temp2)
        result_low.append(low_quantile)
        result_high.append(high_quantile)
    return result_low, result_high


# def model(df):
#     # 获取最后一列  业务量
#     D_series = df.iloc[:, -1]
#     low_quantile, high_quantile = Warningfun_main(D_series)
#     df['low_quantile'] = low_quantile
#     df['high_quantile'] = high_quantile
#     return df


# 线上预测
if __name__ == '__main__':
    def model_predict(df):
        # 获取业务量数据
        D_df = df.iloc[:, -1]
        low_quantile, high_quantile = Warningfun_main(D_df)
        df['low_quantile'] = low_quantile
        df['high_quantile'] = high_quantile
        return df


def plot_fun(df, index=0):
    plt.figure()  # 创建画布
    real_ts = df.iloc[-200:, 0]
    plt.plot(real_ts, color='r', linestyle='-', label='real')
    predict_up = df.iloc[-200:, 1]
    predict_down = df.iloc[-200:, 2]
    plt.plot(predict_up, color='g', linestyle='--', label='predict_up')
    plt.plot(predict_down, color='g', linestyle='--', label='predict_down')
    plt.legend()
    plt.savefig('plot_' + str(index) + '.jpg')


# 计算比例方差
def std_avg(df):
    # 归一化操作
    df['x'] = df.iloc[:, 0] - df.iloc[:, 1]
    df['x1'] = (df['x'] - df['x'].mean()) / df['x'].std()
    arr_std = np.std(df['x1'][-200:], ddof=1)
    return arr_std


# 计算比例方差
def std_avg_to(df):
    # 归一化操作
    df['x'] = df.iloc[:, 0] - df.iloc[:, 1]
    # print(df['x'])
    df['x1'] = (df['x'] - df['x'].mean()) / df['x'].std()
    return df


data1 = data1[['日期', '时间', '业务量']]
data1 = model_predict(data1)
data1 = std_avg_to(data1[['业务量', 'low_quantile', 'high_quantile']])

data2 = data2[['日期', '时间', '总业务量']]
data2 = model_predict(data2)
data2 = std_avg_to(data2[['总业务量', 'low_quantile', 'high_quantile']])

data3 = data3[['轮次', '业务', '接收第三方渠道交易量']]
data3 = model_predict(data3)
data3 = std_avg_to(data3[['接收第三方渠道交易量', 'low_quantile', 'high_quantile']])

data4 = data4[['轮次', '业务', '接收第三方渠道交易量']]
data4 = model_predict(data4)
data4 = std_avg_to(data4[['接收第三方渠道交易量', 'low_quantile', 'high_quantile']])

data5 = data5[['轮次', '总业务量']]
data5 = model_predict(data5)
data5 = std_avg_to(data5[['总业务量', 'low_quantile', 'high_quantile']])

# 测试数据
data6 = data6[['日期', '时间', '业务量']]
data6 = model_predict(data6)
data6 = std_avg_to(data1[['业务量', 'low_quantile', 'high_quantile']])

#  计算差值波动方差
std_1 = std_avg(data1[['业务量', 'low_quantile', 'high_quantile']])
std_2 = std_avg(data2[['总业务量', 'low_quantile', 'high_quantile']])
std_3 = std_avg(data3[['接收第三方渠道交易量', 'low_quantile', 'high_quantile']])
std_4 = std_avg(data4[['接收第三方渠道交易量', 'low_quantile', 'high_quantile']])
std_5 = std_avg(data5[['总业务量', 'low_quantile', 'high_quantile']])
std_6 = std_avg(data6[['业务量', 'low_quantile', 'high_quantile']])
# print([std_1, std_2, std_3, std_4, std_5, std_6])

# 画图1
plt.figure()
std_ts1 = data1.iloc[-200:, -1].reset_index(drop=True)
std_ts2 = data2.iloc[-200:, -1].reset_index(drop=True)
std_ts3 = data3.iloc[-200:, -1].reset_index(drop=True)
std_ts4 = data4.iloc[-200:, -1].reset_index(drop=True)
std_ts5 = data5.iloc[-200:, -1].reset_index(drop=True)
# 测试数据
std_ts6 = data6.iloc[-200:, -1].reset_index(drop=True)
plt.plot(std_ts1, label='0.3')
plt.plot(std_ts2, label='0.5745')
plt.plot(std_ts3, label='0.9687')
plt.plot(std_ts4, label='0.4952')
plt.plot(std_ts5, label='1.05')
# 测试数据
plt.plot(std_ts6, label='0.5')
plt.legend()
plt.savefig('plot_0.jpg')

import mpl_toolkits.axisartist.axislines as axislines

plt.figure()  # 创建画布
std_ts1 = data1.iloc[-200:, -1].reset_index(drop=True)
std_ts2 = data2.iloc[-200:, -1].reset_index(drop=True)
std_ts3 = data3.iloc[-200:, -1].reset_index(drop=True)
std_ts4 = data4.iloc[-200:, -1].reset_index(drop=True)
std_ts5 = data5.iloc[-200:, -1].reset_index(drop=True)
# 测试数据
std_ts6 = data6.iloc[-200:, -1].reset_index(drop=True)
fig, ax1 = plt.subplots(figsize=(10, 10))
plt.subplot(611)
plt.plot(std_ts1, label='0.3')
plt.ylim(-2, 3)
plt.legend()
plt.subplot(612)
plt.plot(std_ts4, label='0.4952')
plt.ylim(-2, 3)
plt.legend()
plt.subplot(613)
plt.plot(std_ts2, label='0.5745')
plt.ylim(-2, 3)
plt.legend()
plt.subplot(614)
plt.plot(std_ts3, label='0.9687')
plt.ylim(-2, 3)
plt.legend()
plt.subplot(615)
plt.plot(std_ts5, label='1.05')
plt.ylim(-2, 3)
# 测试数据
plt.subplot(616)
plt.plot(std_ts6, label='0.5')
plt.ylim(-2, 3)
plt.legend()
plt.savefig('plot_00.jpg')

# 画图
# plot_fun(data1[['业务量', 'low_quantile', 'high_quantile']], index=11)
# plot_fun(data2[['总业务量','low_quantile','high_quantile']],index=21)
# plot_fun(data3[['接收第三方渠道交易量','low_quantile','high_quantile']],index=31)
# plot_fun(data4[['接收第三方渠道交易量','low_quantile','high_quantile']],index=41)
# plot_fun(data5[['总业务量','low_quantile','high_quantile']],index=51)
# plot_fun(data6[['业务量', 'low_quantile', 'high_quantile']], index=61)
