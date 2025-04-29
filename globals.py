import pandas as pd
import os

# Verifica se os arquivos de despesas e receitas já existem, se não existir cria os arquivos com a estrutura padrão
if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=['Data'])
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=['Data'])
    df_receitas['Data'] = pd.to_datetime(df_receitas['Data'])
    df_despesas['Data'] = pd.to_datetime(df_despesas['Data'])
    df_receitas['Data'] = df_receitas['Data'].apply(lambda x: x.date())
    df_despesas['Data'] = df_despesas['Data'].apply(lambda x: x.date())
else:
    data_structure = {'Valor': [],
        'Efetuado': [],
        'Fixo': [],
        'Data': [],
        'Categoria': [],
        'Descrição': [],}
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_despesas.to_csv("df_despesas.csv")
    df_receitas.to_csv("df_receitas.csv")

# Verifica se os arquivos de categorias já existem, se não existir cria os arquivos com as categorias padrão
if ("df_cat_despesas.csv" in os.listdir()) and ("df_cat_receitas.csv" in os.listdir()):
    df_cat_despesas = pd.read_csv("df_cat_despesas.csv", index_col=0)
    df_cat_receitas = pd.read_csv("df_cat_receitas.csv", index_col=0) 
    cat_receita = df_cat_receitas.values.tolist()
    cat_despesa = df_cat_despesas.values.tolist()
else:
    cat_receita = {'Categoria': ["Salário", "Investimentos", "Comissão"]}
    cat_despesa = {'Categoria': ["Alimentação", "Transporte", "Saúde", "Educação", "Lazer", "Imprevistos", "Aluguel"]}
    df_cat_receitas = pd.DataFrame(cat_receita)
    df_cat_despesas = pd.DataFrame(cat_despesa)
    df_cat_despesas.to_csv("df_cat_despesas.csv")
    df_cat_receitas.to_csv("df_cat_receitas.csv")