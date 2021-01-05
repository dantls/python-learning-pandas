import pandas as pd

# Series
serie_receita = pd.Series(data = [1,4,2,10,1000,None], name='receita')

# Mostrando a série criada
print("Nossa serie:", serie_receita)
print("Nossa serie:", serie_receita)
print("Tipo da nossa serie:", type(serie_receita))

# DataFrame

dados = { "nome": ['Danilo', 'Franciele'],
          "sobrenome": ['Gomes', 'Teixeira'],
          "idade": [29, 28] }

print(dados)
df_pessoas = pd.DataFrame(dados)
print(df_pessoas)

#Lendo um .csv

pathfile_csv = "/home/dan_tls/pandas/data/tb_candidatura_2018.csv"
df_candidatura = pd.read_csv(pathfile_csv ,sep=";")
df_candidatura.head()

#Lendo um .xlsx
pathfile_xlsx = "/home/dan_tls/pandas/data/tb_declaracao_2018.xlsx"
df_declaracao = pd.read_excel(pathfile_xlsx)

#Número de linha para serem exibidas
df_declaracao.head(2)

#As últimas linhas a serem exibidas
df_declaracao.tail(2) #Isso é um método

#Número de linhas e colunas de um dataframe(tupla)
df_declaracao.shape 

df_declaracao.shape[0] #Isso é um atributo (quantidade de linhas)
df_declaracao.shape[1] #Isso é um atributo (quantidade de colunas)

# Quais são as colunas do dataframe?
df_declaracao.columns #Retorna os indices das colunas do dataframe


#Navegando pelas colunas do DataFrame
df_declaracao['descricao_tipo'] #Retorna a coluna solicitada


#Pegando x colunas
df_declaracao[['descricao_tipo', 'detalhe']] 
#Isso gera um novo DataFrame