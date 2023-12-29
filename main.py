# Primeiro vamos importar as bibliotecas necessárias e usar alias para criar "apelidos"
import pandas as pd
import matplotlib.pyplot as plt

# setando configurações para facilitar a visualização no PyCharm (plataforma adotada)
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 200)

# Formatando a saida dos dados com valores muito grandes
pd.options.display.float_format = '{:20,.2f}'.format

# Configurando o estilo dos gráficos que serão gerados futuramente
plt.style.use("seaborn-v0_8")

# Lendo o arquivo em excel e criando o dataframe
df = pd.read_excel("datasets/AdventureWorks.xlsx")
# O menor da coluna venda total
print(df.head(5))  # Imprimindo as 5 primeiras linhas do DataFrame

print(df.tail(5))  # Imprimindo as 5 ultimas linhas do DataFrame

print(df.dtypes)  # Conferindo os tipos de cada coluna

print(df.shape)  # visualizando o formato do df

print(df.columns)  # visuzalizando as colunas do df

print(df.describe())  # Visão geral sobre o df, contendo média, máxima, minima, e etc...

print(df['Produto'].unique())  #Retorna todos os valores unicos da coluna Produto

# Criando um dataframe que contem apenas as linhas com a marca Fabrikam
Fabrikam_only = df.loc[df["Marca"] == 'Fabrikam']
print(Fabrikam_only.head(5))

print(df["Marca"].unique())  # Printando todos os valores unicos na coluna Marca

print(df.groupby('Fabricante')['Produto'].nunique())  # Contando quantidade de produtos diferentes por marca

print(df.groupby('ID Loja')['Valor Venda'].sum())  # Encontrando o lucro total de cada loja

# Média dos valores de venda de cada loja nos respectivos anos
print(df.groupby([df['Data Venda'].dt.year, 'ID Loja'])['Valor Venda'].mean())

### Graficos ###

df.groupby([df['Data Venda'].dt.year, 'ID Loja'])['Valor Venda'].mean().plot.barh(title="Média de vendas por loja em 2008 ~ 2009")
plt.xlabel('Vendas')
plt.ylabel('Ano, ID Loja')
plt.savefig("Graficos\main\Graf-01.png")
plt.show()

df.groupby('ID Loja')['Quantidade'].sum().plot.bar(title="Vendas por Loja")
plt.xlabel("ID da Loja")
plt.ylabel("Vendas")
plt.xticks(rotation="horizontal")
plt.savefig("Graficos\main\Graf-02.png")
plt.show()