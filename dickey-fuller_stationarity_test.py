# Perform Dickey-Fuller test:
'''
This conducts an ADCF test for stationarity
for time series analysis.

Replace 'data' and 'column' with 
context-specific values.
'''

from statsmodels.tsa.stattools import adfuller

print('Dickey-Fuller Results:')
dftest = adfuller(data.column, autolag='AIC')

dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', 'Number of Lags Used', 
                                         'Number of Observations Used'])

# use a loop to append critical values by significance level to the output
for key, value in dftest[4].items():
    dfoutput['Critical Value (%s)'%key] = value
    
# print the test results
print(dfoutput)