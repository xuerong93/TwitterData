import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import csv
import numpy as np
from statsmodels.tsa.stattools import adfuller

tweets_data_path1 = 'TrumpTrain_trend.csv'


tweets_data1 = []

tweets_file1 = open(tweets_data_path1,"r")

for line in tweets_file1:
    lines = line.split(',')
    try:
        lines[0] = pd.to_datetime(lines[0].strip('\r\n'))
        if line:
            tweets_data1.append(lines[0])
    except:
        continue
        


print len(tweets_data1)

ones1 = [1]*len(tweets_data1)
idx1 = pd.DatetimeIndex(tweets_data1)
l1=pd.Series(ones1,index=idx1)
per_minute1 = l1.resample('1min').sum().fillna(0)


per_minute.plot()    
plt.show()   

# per_tenMin1 = per_minute1[0:len(per_minute1)-1]
# per_tenMin2 = per_minute2[0:len(per_minute2)-1]

# per_tenMincsv1 = []
# per_ten1=[]
# for i in xrange(len(per_tenMin1)):
    # per_tenMincsv1 += [[i,per_tenMin1[i]]]
    # per_ten1 += [per_tenMin1[i]]

# per_tenMincsv2 = []
# per_ten2=[]
# for i in xrange(len(per_tenMin2)):
    # per_tenMincsv2 += [[i,per_tenMin2[i]]]
    # per_ten2 += [per_tenMin2[i]]
    
# with open("TrumpTrain_trend1.csv", "wb") as f:
    # writer = csv.writer(f)
    # writer.writerows(per_tenMincsv1)
# with open("VoteTrump_trend1.csv", "wb") as f:
    # writer = csv.writer(f)
    # writer.writerows(per_tenMincsv2)
#print np.correlate(per_ten1, per_ten2)
# plt.plot(per_ten1,per_ten2)
# plt.show()


# def test_stationarity(timeseries):
    
    # #Determing rolling statistics
    # #rolmean = pd.rolling_mean(timeseries, window=12)
    # #rolstd = pd.rolling_std(timeseries, window=12)
    # rolmean = timeseries.rolling(window=12,center=False).mean()
    # rolstd = timeseries.rolling(window=12,center=False).std()

    # #Plot rolling statistics:
    # orig = plt.plot(timeseries, color='blue',label='Original')
    # mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    # std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    # plt.legend(loc='best')
    # plt.title('Rolling Mean & Standard Deviation')
    # plt.show(block=True)
    
    # #Perform Dickey-Fuller test:
    # print 'Results of Dickey-Fuller Test:'
    # dftest = adfuller(timeseries, autolag='AIC')
    # dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    # for key,value in dftest[4].items():
        # dfoutput['Critical Value (%s)'%key] = value
    # print dfoutput
    
# test_stationarity(per_tenMin1)


# ts=per_tenMin1
# ts_log = np.log(ts)
# # plt.plot(ts_log)
# moving_avg = ts_log.rolling(12).mean()
# plt.plot(ts_log)
# plt.plot(moving_avg, color='green')
# ts_log_moving_avg_diff = ts_log - moving_avg
# ts_log_moving_avg_diff.dropna(inplace=True)
# test_stationarity(ts_log_moving_avg_diff)


# expwighted_avg = ts_log.ewm(halflife=12,ignore_na=False,min_periods=0,adjust=True).mean()
# plt.plot(ts_log)
# plt.plot(expwighted_avg, color='green')
# ts_log_ewma_diff = ts_log - expwighted_avg
# test_stationarity(ts_log_ewma_diff)

# #diffirential
# ts_log_diff = ts_log - ts_log.shift()
# plt.plot(ts_log_diff)
# ts_log_diff.dropna(inplace=True)
# test_stationarity(ts_log_diff)

# #ACF and PACF plots:
# from statsmodels.tsa.stattools import acf, pacf
# lag_acf = acf(ts_log_diff, nlags=20)
# lag_pacf = pacf(ts_log_diff, nlags=20, method='ols')
# #Plot ACF: 
# plt.subplot(121) 
# plt.plot(lag_acf)
# plt.axhline(y=0,linestyle='--',color='gray')
# plt.axhline(y=-1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
# plt.axhline(y=1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
# plt.title('Autocorrelation Function')
# #Plot PACF:
# plt.subplot(122)
# plt.plot(lag_pacf)
# plt.axhline(y=0,linestyle='--',color='gray')
# plt.axhline(y=-1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
# plt.axhline(y=1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
# plt.title('Partial Autocorrelation Function')
# plt.tight_layout()

# from statsmodels.tsa.arima_model import ARIMA
# #AR
# model = ARIMA(ts_log, order=(2, 1, 0))  
# results_AR = model.fit(disp=-1)  
# plt.plot(ts_log_diff)
# plt.plot(results_AR.fittedvalues, color='red')
# plt.title('RSS: %.4f'% sum((results_AR.fittedvalues-ts_log_diff)**2))

# #combination
# model = ARIMA(ts_log, order=(0, 1, 2))  
# results_MA = model.fit(disp=-1)  
# plt.plot(ts_log_diff)
# plt.plot(results_MA.fittedvalues, color='red')
# plt.title('RSS: %.4f'% sum((results_MA.fittedvalues-ts_log_diff)**2))

# #MA
# model = ARIMA(ts_log, order=(2, 1, 2))  
# results_ARIMA = model.fit(disp=-1)  
# plt.plot(ts_log_diff)
# plt.plot(results_ARIMA.fittedvalues, color='red')
# plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-ts_log_diff)**2))


# predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
# print predictions_ARIMA_diff.head()
# predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
# print predictions_ARIMA_diff_cumsum.head()
# predictions_ARIMA_log = pd.Series(ts_log.ix[0], index=ts_log.index)
# predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum,fill_value=0)
# predictions_ARIMA_log.head()
# predictions_ARIMA = np.exp(predictions_ARIMA_log)
# plt.plot(ts)
# plt.plot(predictions_ARIMA)
# plt.title('RMSE: %.4f'% np.sqrt(sum((predictions_ARIMA-ts)**2)/len(ts)))