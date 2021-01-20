#  实际值和预测值的比较
import pandas as pd
import numpy as np
# 数据导入
#一级能开业务量数据、统一接口平台业务量，统一支付_支付业务量，
f1 = open('一级能开业务量.csv')
f2 = open('统一接口平台业务量.csv')
f3 = open('统一支付_在线扣费业务.csv')
f4 =open('统一支付_支付业务.csv')
data1 = pd.read_csv(f1)
data2 = pd.read_csv(f2)
data3 = pd.read_csv(f3)
data4 = pd.read_csv(f4)

data5 = pd.read_excel('PBOSS.xlsx')



#设置预测值，根据
# 1.2倍四分位方差，计算异常值
# 根据10天的


def Warningfun(series):
    # 计算上下四分位数
    Q1 = series.quantile(q=0.25)
    Q3 = series.quantile(q=0.75)
    # 异常值判断标准， 1.5倍的四分位差 计算上下须对应的值
    low_quantile = Q1 - 1.2 * (Q3 - Q1)
    high_quantile = Q3 + 1.2 * (Q3 - Q1)
    # 输出异常值
    return low_quantile, high_quantile

def Warningfun_main(series):
    s_len  = len(series)
    inv_t = 24 * 2
    day_num = 10 * inv_t
    # end_tage = s_len-inv_t
    result_low = list(series[0:day_num])
    result_high = list(series[0:day_num])
    for index in  range(day_num,s_len):
        # index = 959
        # print(index)
        series_temp = series[(index - day_num):index].reset_index(drop=True)
        # index_flage = np.linspace(0, day_num, num=int(day_num / inv_t) + 1, dtype=int)
        series_temp2 = series_temp[np.linspace(0, day_num-1, num=int(day_num / inv_t) + 1, dtype=int)]  #获取同比数据
        low_quantile, high_quantile = Warningfun(series_temp2)
        result_low.append(low_quantile)
        result_high.append(high_quantile)
    return result_low ,result_high

D_series = data1.iloc[:,4]
low_quantile, high_quantile = Warningfun_main(D_series)
data1['low_quantile'] = low_quantile
data1['high_quantile'] = high_quantile

