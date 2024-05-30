#Utilizar a tabela de dados do clima de seu estado, 
# manipule os dados de acordo com as instruções abaixo: 
# 1. calcular a média da temperatura da amostra, ok
# 2. retirar nulos da coluna 'RADIACAO GLOBAL (Kj/m2)', 
# 3. copiar o dataframe reduzindo para 3 colunas (a sua escolha) e 1000 linhas (aleatórias) - 
# 4. Bônus: normalizar coluna (qualquer uma)
# 5. Bônus II: pesquisar sobre outras formas de processamento de dados além das vistas em sala de aula


import pandas as pd

df = pd.read_csv('data_sample_PI.csv', sep=';' , encoding='UTF-8')
media_temperatura = df['TEMPERATURA DO AR - BULBO SECO. HORARIA (C)'].median()
print("1. Calcular a média da temperatura da amostra.")
print(f"Média da temperatura: {media_temperatura} graus Celsius")
print("\n")
# A temperatura do bulbo seco do ar é a temperatura medida com um termômetro comum.
# A temperatura de bulbo úmido (a temperatura mínima em que a água se evapora naquele momento)

df_nan = df.dropna(subset=['RADIACAO GLOBAL (Kj/m2)'])
print("2. Retirar nulos da coluna 'RADIACAO GLOBAL (Kj/m2)'.")
print(df_nan['RADIACAO GLOBAL (Kj/m2)'])
print("\n")



df_menor = df[['TEMPERATURA DO AR - BULBO SECO. HORARIA (C)', 'RADIACAO GLOBAL (Kj/m2)', 'VENTO. RAJADA MAXIMA (m/s)']].sample(n=1000, random_state=1)
df_menor = df_menor.reset_index(drop=True)
print("3. Copiar o dataframe reduzindo para 3 colunas (a sua escolha) e 1000 linhas (aleatórias)")
print(df_menor)


df = df.copy()
coluna = 'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO. HORARIA (mB)'
df[coluna] = df[coluna] / df[coluna].abs().max()
print("4. Bônus: normalizar coluna (qualquer uma)")
print(df)



# 5. Bônus II: pesquisar sobre outras formas de processamento de dados além das vistas em sala de aula
#O processamento de dados envolve a transformação de dados brutos em informações.
#Processamento em lote: O sistema divide uma grande quantidade de dados em unidades/lotes menores antes de coletá-los e processá-los.
#Processamento em tempo real: Normalmente, envolve o processamento e a transferência de dados assim que o sistema os obtém, para auxiliar na rápida tomada de decisões.
#Processamento on-line: Envolve o processamento automático de dados inserindo-os automaticamente por meio de uma interface assim que estiverem disponíveis.
#Multiprocessamento: Dividir um sistema de computador em processadores menores para distribuir o processamento de dados entre eles, garantindo uma execução coerente. Os engenheiros de dados também se referem a isso como processamento paralelo.
#Compartilhamento de tempo: Permitir que vários usuários acessem o sistema do computador simultaneamente, para executar o processo.

