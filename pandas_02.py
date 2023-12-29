import pandas as pd
import matplotlib.pyplot as plt

# setando configurações para facilitar a visualização no PyCharm (plataforma adotada)
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 200)

# Formatando a saida dos dados com valores muito grandes

# Criando os dataframes
df1 = pd.read_excel('datasets/Natal.xlsx')
df2 = pd.read_excel('datasets/Salvador.xlsx')
df3 = pd.read_excel('datasets/Recife.xlsx')
df4 = pd.read_excel('datasets/Aracaju.xlsx')
df5 = pd.read_excel('datasets/Fortaleza.xlsx')


df = pd.concat([df1, df2, df3, df4, df5])  # Concatenando os 5 dataframes em um só

# print(df.dtypes)

df = df.rename(columns={'Cidade':'Cidade', 'Data':'Data', 'Vendas':'Valor', 'LojaID':'LojaID', 'Qtde':'Qtde'})  # Renomeando as colunas

# print(df.isnull().sum())  # Conferindo se há valores nulosdf["Valor"].fillna(df["Vendas"].mean(), inplace=True)  # Substituindo pela média da coluna valor

"""
Podemos substituir os valores nulos por:
    - Zeros = df["Valor"].fillna(0, inplace=True)
    - Media da própria coluna, caso seja int64 = df["Valor"].fillna(df["Valor"].mean(), inplace=True)
    - Podemos APAGAR completamente as linhas que possuem valores invalidos = df.dropna(inplace=True)
"""

df["Valor"].fillna(df["Valor"].mean(), inplace=True)  # Substituindo pela média da coluna valor

df['Valor Total'] = df['Valor'].mul(df["Qtde"])  # Criando nova coluna

#print(df["Valor Total"].min())  # O menor da coluna venda total

#print(df["Valor Total"].max())  # O maior da coluna venda total

df["Mês Venda"], df["Dia Venda"] = (df["Data"].dt.month, df["Data"].dt.day)  # Criando duas colunas (Mês e Dia da venda)

df["Trimestre"] = df['Data'].dt.quarter  # Criando uma coluna que registra o trimestre do ano

trim = df.loc[df['Trimestre'] == 3]  # Criando um dataframe que recebe apenas dados que estão no 3 semestre

df_2018 = df.loc[df["Data"].dt.year == 2018]

print(df["LojaID"].value_counts(ascending=False))  # Conta cada linha contendo cada LojaID e retorna

### Gráficos ###

# Grafico de barras na vertical
df["LojaID"].value_counts(ascending=False).plot.bar(title="Ocorrências de cada LojaID")
plt.savefig("Graficos/main_02/Graf_01.png")
plt.show()

# Grafico de barras na horizontal e em vermelho
df["LojaID"].value_counts(ascending=False).plot.barh(title="Ocorrências de cada LojaID", color='red')
plt.savefig("Graficos/main_02/Graf_02.png")
plt.show()

# Produtos totais vendido por Mês
df.groupby("Data")['Qtde'].sum().plot(title="Total de produtos vendidos por mês", color='purple')
plt.savefig("Graficos/main_02/Graf_03.png")
plt.show()

# Adição de "o"
df.groupby("Data")['Qtde'].sum().plot(title="Total de produtos vendidos por mês", color='purple', marker='o')
plt.savefig("Graficos/main_02/Graf_04.png")
plt.show()

# Scatter
plt.scatter(x = df_2018["Trimestre"], y = df_2018["Valor Total"])
plt.savefig("Graficos/main_02/Graf_05.png")
plt.show()
