# Importe das bibliotecas necessarias
import yfinance as yf
from datetime import datetime
import pandas as pd

# Função para obter os preços das commodities
def GetCommodities_price():
    symbols = ["GC=F", "CL=F", "SI=F"]
    dfs = []
    for syn in symbols:
        ticker = yf.Ticker(syn)  # Ouro
        hist = ticker.history(period="1d", interval="1m")
        
        # Pega o ultimo preco disponivel
        ultimo_preco = round(float(hist['Close'].iloc[-1]), 2)
        
        # Cria o DataFrame com os dados
        ativo = syn
        preco = ultimo_preco
        moeda = 'USD'
        horario_coleta = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Os valores são retornados em um dicionário
        valores = {'ativo': ativo, 'preco': preco, 'moeda': moeda, 'horario_coleta': horario_coleta}
        dfs.append(valores) # a lista de dicionários é retornada para ser usada posteriormente
  
    return dfs