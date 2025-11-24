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

# Função para preparar e salvar os dados 
def dataPrepared(valores):
    # Se for uma lista, ele extrai os dicionários da lista antes de salvar cada dicionário
    if isinstance(valores, list):
        for item in valores:
            salvar_cotacao(
                ativo=item['ativo'],
                preco=float(item['preco']),
                moeda=item['moeda'],
                horario_coleta=item['horario_coleta'],
                dataIngest=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )
    # Se for um dicionário, salva diretamente
    elif isinstance(valores, dict):
        salvar_cotacao(
            ativo=valores['ativo'],
            preco=float(valores['preco']),
            moeda=valores['moeda'],
            horario_coleta=valores['horario_coleta'],
            dataIngest=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

dataPrepared(valores_Commodities)
dataPrepared(valores_Bitcoin)
