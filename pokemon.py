import pandas as pd


df = pd.read_csv('pokemon_data.csv')

#print(df)
#print(df.head())
#print(df.columns)
#print(df[['Nombre','Tipo  1','Vida']])
#print(df.iloc[1:4])
#for index,row in df.iterrows():
#	print(index,row['Nombre'])
#print(df.loc[df['Tipo 1']=='fuego'])
#print(df.describe())
#print(df.sort_values('Nombre',ascending=False)) 
#df['total']=df['Vida']+df['Ataque']
#print(df.head(5)) 


print(df['Vida','Nombre'].head(5))
