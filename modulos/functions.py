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
    
    df['retorno_dia'] = (df['Close'] - df['Open']) / df['Open'] * 100 # Retorno diário (%)

    df['amplitude'] = (df['High'] - df['Low']) / df['Open'] * 100 # Amplitude do dia (%)

    # Médias móveis
    # df['sma_3'] = df['Close'].rolling(window=3).mean()
    # df['sma_7'] = df['Close'].rolling(window=7).mean()

    # df['retorno_3dias'] = (df['Close'] - df['Close'].shift(3)) / df['Close'].shift(3) * 100 # Retorno acumulado 3 dias

    # df['volatilidade_5d'] = df['Close'].rolling(window=5).std() # Volatilidade (desvio padrão dos últimos 5 dias)

    # df['volume_relativo'] = df['Volume'] / df['Volume'].rolling(window=5).mean() # Volume relativo (comparado à média dos últimos 5 dias)

    df = df.dropna() # Remove as primeiras linhas que ficaram com NaN por causa dos cálculos de rolling e shift

    print(df.head()) # Verificar se está tudo certo

    return df

