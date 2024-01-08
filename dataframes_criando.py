### Definição: Uma tabala de dados. Um objeto bi-dimensional que tem dados de forma tabular (EXCEL)

import pandas as pd 
import numpy as np

## Criando DataFrames: 

df1=pd.DataFrame()

#Criando um dicionário para criar um DataFrame em seguida:
dict1={'identificação':[1,2,3,4,5],
       'nome':['Caio','Rodrigo','Rafael','Mariane','Nathane']}

#Transformando o dicionário em um DataFrame:
df2=pd.DataFrame(data=dict1)

#Fazendo mudanças no index da tabela : 
df3=pd.DataFrame(data=dict1,index= [29,1,0,2222,88])

#Coluna que podemos criar no nosso DataFrame:
serie1=pd.Series([1,2,3])

serie2=pd.Series(['a','b','c'])

df4=pd.DataFrame({'coluna1':serie1,
                  'coluna2':serie2})

array1 = np.array([
    [1, 2, 3],
    ['São Paulo', 'Rio de Janeiro', 'Campinas'],
    ['SP', 'RJ', 'SP']
])

df5=pd.DataFrame(data=array1.transpose (),
                 index=['linha1','linha2','linha3'],
                 columns=['identificação','cidade','estado'])

matriz1=np.matrix([1,2,3],
                  ['São Paulo','Rio de Janeiro','Campinas'],
                  ['SP','RJ','SP'])
