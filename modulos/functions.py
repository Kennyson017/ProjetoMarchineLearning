import yfinance as yf
import pandas as pd
import modulos.config as config

# Buscado de dados do Yfinance gerando o CSV -------------
def create_csv():
    dados = yf.download(
    config.ticker,
    start = config.start_date,
    end = config.end_date)

    # print(dados.head())

    dados.to_csv(fr"{config.path}\{config.ticker}_{config.start_date}_to_{config.end_date}.csv")


# Tratamento de CSV importado do yfinance -------------
def treat_csv():

    fileCSV = fr"database\{config.ticker}_{config.start_date}_to_{config.end_date}.csv"

    df = pd.read_csv(fileCSV, skiprows=[1,2])
    df = df.rename(columns={'Price': 'Date'})

    df['Ticker'] = config.ticker # Cria coluna de nome do ativo
    df['Date'] = pd.to_datetime(df['Date']) # Converte pro formate data
    df['Target'] = (df['Close'] > df['Open']).astype(int) # Cria coluna do atributo alvo
    df['Retorno_real'] = (df['Close'] - df['Open']) / df['Open'] * 100

    # print(df.head())

    df.to_csv(fr"database\tratado_{config.ticker}.csv", index=False)

    return df
