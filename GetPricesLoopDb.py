# Importe das bibliotecas necessárias
from GetBitcoin import get_bitcoin_price
from GetCommodities import GetCommodities_price

import os
from sqlalchemy import create_engine, Table, Column, Integer, String, Numeric, MetaData, TIMESTAMP, BigInteger
from dotenv import load_dotenv
from datetime import datetime

# Carrega variáveis do .env
load_dotenv()

# Configura engine
engine = create_engine(
    "postgresql+psycopg2://",
    connect_args={
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASS"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "dbname": os.getenv("DB_NAME")
    }
)

# Define metadados e tabela
metadata = MetaData()

FinancialMarketPrice = Table(
    'FinancialMarketPrice', metadata,
    Column("idTransacao", BigInteger, primary_key=True),
    Column("ativo", String, nullable=False),
    Column("preco", Numeric, nullable=False),
    Column("moeda", String, nullable=False),
    Column("horario_coleta", TIMESTAMP, nullable=False),
    Column("dataIngest", TIMESTAMP, nullable=False)
)

def salvar_cotacao(ativo: str, preco: float, moeda: str, horario_coleta: datetime, dataIngest: datetime):
    """Insere uma cotacao no banco de dados"""
    with engine.connect() as conn:
        conn.execute(
            FinancialMarketPrice.insert(),
            {
                "ativo": ativo,
                "preco": preco,
                "moeda": moeda,
                "horario_coleta": horario_coleta,
                "dataIngest": dataIngest
            }
        )
        conn.commit()
