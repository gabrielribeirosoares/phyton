import pandas as pd
encoding='utf-8'
from pandas.core.reshape import encoding

# Carrega a planilha do Excel
caminho_planilha = 'C:\aula_hoje\Tabelas_panorama\censo'
dados = pd.read_excel(caminho_planilha)


# Visualiza as primeiras linhas da planilha
print("Primeiras 5 linhas da planilha:")
print(dados.head())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(dados.describe())

# Informações sobre as colunas
print("\nInformações sobre as colunas:")
print(dados.info())

# Média de uma coluna específica
nome_coluna = 'População feminina(pessoas)'
media_coluna = dados[nome_coluna].mean()
print(f"\nMédia da coluna {nome_coluna}: {media_coluna}")

# Filtragem de dados
filtro = dados['População feminina(pessoas)']
dados_filtrados = dados[filtro]
print("\nDados filtrados:")
print(dados_filtrados)

# Salvar dados filtrados em uma nova planilha
caminho_nova_planilha = 'C:\aula_hoje\aulanova.xlsx'
dados_filtrados.to_excel(caminho_nova_planilha, index=False)

print("Análise concluída.")

