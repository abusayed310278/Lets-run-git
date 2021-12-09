import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras import metrics

from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('Google.csv')

L=len(df)
print(L)

Hi = np.array([df.iloc[:,2]])
Low = np.array([df.iloc[:,3]])
Close = np.array([df.iloc[:,4]])

plt.figure(1)
H, = plt.plot(Hi[0,:])
L, = plt.plot(Low[0,:])
C, = plt.plot(Close[0,:])

plt.legend([H,L,C],["High","Low","CLose"])
plt.show(block=False)

#plt.waitKey(0)