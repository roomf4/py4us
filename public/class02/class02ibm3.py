# class02ibm3.py

# This script should Create a list of 2016-11 IBM prices
# This script should Create a list of dates of those prices
# This script should Create a plot of the prices

# Ref:
# https://finance.yahoo.com/quote/IBM/history?p=IBM

# Demo:
# python class02ibm3.py

import pdb

prices_l = [
  162.220001
  ,163.529999
  ,164.520004
  ,163.139999
  ,161.979996
  ,162.669998
  ,162.770004
  ,160.389999
  ,159.800003
  ,159.289993
  ,158.669998
  ,158.210007
  ,161.270004
  ,160.220001
  ,154.809998
  ,155.169998
  ,155.720001
  ,152.429993
  ,152.369995
  ,151.949997
  ,152.789993
]

dates_s_l = [
  '2016-11-30'
  ,'2016-11-29'
  ,'2016-11-28'
  ,'2016-11-25'
  ,'2016-11-23'
  ,'2016-11-22'
  ,'2016-11-21'
  ,'2016-11-18'
  ,'2016-11-17'
  ,'2016-11-16'
  ,'2016-11-15'
  ,'2016-11-14'
  ,'2016-11-11'
  ,'2016-11-10'
  ,'2016-11-09'
  ,'2016-11-08'
  ,'2016-11-07'
  ,'2016-11-04'
  ,'2016-11-03'
  ,'2016-11-02'
  ,'2016-11-01'
]

pdb.set_trace()
print(dates_s_l)
print(prices_l)

# I should plot prices on y-axis vs dates on x-axis:
import matplotlib.pyplot as plt
plt.plot(prices_l)
plt.show()

'bye'
