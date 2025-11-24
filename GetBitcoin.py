# Importe das bibliotecas necessarias
import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_price():
    # URL Para obtencao do preoo
    url = 'https://api.coinbase.com/v2/prices/spot'
    
    # Requisicao do preco
    response = requests.get(url)
    data = response.json()
    
  
    preco = round(float(data['data']['amount']), 2)
    ativo = data['data']['base']
    moeda = data['data']['currency']
    horario_coleta = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    valores = {'ativo': ativo, 'preco': preco, 'moeda': moeda, 'horario_coleta': horario_coleta}
    
    df = pd.DataFrame([valores]) 

    return df


