import pandas as pd
import matplotlib as plt

data = pd.read_csv('car.csv',header=None)

data.columns=['Price','Maintenance','NumberDoos','Capacity','Size Luggage','Safety','Decision']


decision = data['Decision'].value_counts()




data['Price'].unique()

data['Price'].replace(('vhigh','high','med','low'),(4,3,2,1),inplace=True)


print(data['Price'].unique())