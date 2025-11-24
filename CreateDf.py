# Importe das bibliotecas necessarias
import pandas as pd
from GetBitcoin import get_bitcoin_price
from GetCommodities import GetCommodities_price
from GetPricesLoopDb import salvar_cotacao
from datetime import datetime
import os



# Coletar os valores
valores_Bitcoin = get_bitcoin_price()
valores_Commodities = GetCommodities_price()

# Funcao para criar o DataFrame e salvar em CSV
def Cria_df(valores_Bitcoin, valores_Commodities):
    # Se o arquivo ja existe, carrega
    if os.path.exists("cotacao.csv"):
        df = pd.read_csv("cotacao.csv")
    else:
        # Se nao existe, cria vazio com colunas
        df = pd.DataFrame(columns=['ativo', 'preco', 'moeda', 'horario_coleta'])
        df = pd.concat([df, valores_Commodities], ignore_index=True)
        df = pd.concat([df, valores_Bitcoin], ignore_index=True)
    
    # Salvando no banco de dados
    salvar_cotacao(ativo=df['ativo'][0],
                   preco=float(df['preco'][0]),
                   moeda=df['moeda'][0],
                   horario_coleta=df['horario_coleta'][0], 
                   dataIngest=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    
    
    print('Cotacao salva com sucesso no banco de dados!')
    #print(salvar_cota)
    return df

df = Cria_df(valores_Bitcoin, valores_Commodities)





