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

    # print(df.head())

    df.to_csv(fr"database\tratado_{config.ticker}.csv", index=False)

    return df


# Dataframe Feature Engineering -------------
def features_dataframe(df):

    df = df.sort_values('Date') # Garante que os dados estão na ordem correta

    df['retorno_d1'] = df['Close'].shift(1) / df['Open'].shift(1) - 1

    df['retorno_3d_antes'] = df['Close'].shift(1) / df['Close'].shift(4) - 1

    df['sma_3_past'] = df['Close'].shift(1).rolling(window=3).mean()
    df['sma_7_past'] = df['Close'].shift(1).rolling(window=7).mean()

    df['volatilidade_5d_past'] = df['Close'].shift(1).rolling(window=5).std()

    df['volume_relativo_past'] = df['Volume'].shift(1) / df['Volume'].shift(1).rolling(window=5).mean()

    df['gap_abertura'] = df['Open'] / df['Close'].shift(1) - 1
    df['alta_dia_anterior'] = (df['Close'].shift(1) > df['Open'].shift(1)).astype(int)
    df['amplitude_anterior'] = (df['High'].shift(1) - df['Low'].shift(1)) / df['Open'].shift(1)


    df = df.dropna() # Remove as primeiras linhas que ficaram com NaN por causa dos cálculos de rolling e shift

    # print(df.head()) # Verificar se está tudo certo

    return df

