import modulos.functions as mf
from modulos.algoritmos import DecisionTree, RamdomForest

import modulos.config as mc

# mc.ticker = "ITUB4.SA"

# mf.create_csv()

df = mf.treat_csv()

train = df[(df['Date'].dt.year >= 2023) & (df['Date'].dt.year <= 2024)]
test = df[(df['Date'].dt.year == 2025)]

# TREINAMENTO

# Features e Targets dos dataframes
features = ['Open', 'High', 'Low', 'Close', 'Volume']
target = 'Target'

# Treino
x_train = train[features] # features
y_train = train[target] # target

# TESTES
x_test = test[features]
y_test = test[target]

# # Sem Feature Engineering

# print("\nDECISION TREE ----------------\n")
# DecisionTree(x_train, y_train, y_test, x_test)

# print("\nRamdom Forest ----------------\n")
# RamdomForest(x_train, y_train, y_test, x_test)

# Com Feature Engineering

df_FE = df

df_train_FE = df_FE[(df_FE['Date'].dt.year >= 2023) & (df_FE['Date'].dt.year <= 2024)]
test_FE = df_FE[(df_FE['Date'].dt.year == 2025)]

df_train_FE = mf.features_dataframe(df_train_FE)
test_FE = mf.features_dataframe(test_FE)

# features_FE = [
#     'Open', 'High', 'Low', 'Close', 'Volume',
#     'retorno_dia', 'amplitude', 'sma_3', 'sma_7',
#     'retorno_3dias', 'volatilidade_5d', 'volume_relativo'
# ]

features_FE = [
    'Open', 'High', 'Low', 'Close', 'Volume',
    'retorno_dia', 'amplitude'
]


x_train_FE = df_train_FE[features_FE] # features
y_train_FE = df_train_FE[target] # target

# Teste 
x_test_FE = test_FE[features_FE]
y_test_FE = test_FE[target]

# print("\nDECISION TREE com Feature Engineering ----------------\n")
# DecisionTree(x_train_FE, y_train_FE, y_test_FE, x_test_FE)

# print("\nRamdom Forest com Feature Engineering----------------\n")
# RamdomForest(x_train_FE, y_train_FE, y_test_FE, x_test_FE)















# print("Período de treino:", train['Date'].min(), "->", train['Date'].max())
# print("Período de teste:", test['Date'].min(), "->", test['Date'].max())


# 👍1) Escolher um código de ativo da B3 e Baixar 3 anos (2023, 2024 e 2025) de
# dados de cotação histórica do ativo escolhido de granularidade (período) diária.


# 👍2) Para o período selecionado, calcular o atributo alvo através da diferença entre o Peço de Abertura e o Preço de Fechamento. Caso o resultado seja positivo o novo atributo alvo terá o valor de 1. E caso o contrário, o novo atributo alvo terá o valor de 0.

# 👍3) Separar os dados em Treinamento (2023 e 2024) e Teste (2025)

# ⏲️ 4) Escolher na biblioteca sci-kit learn e implementar um algoritmo de aprendizado de máquina categoria supervisionado (classificador) (KNN, DT, NB, SVM e outro).

# ⏲️ 5) Realizar as simulações e ajustar os parâmetros do algoritmo escolhido aos
# dados avaliados.

# 6) Revisar os dados coletados com o objetivo de retirar ruídos e ou atributos
# irrelevantes e, em seguida, proponha uma nova forma de treinar os dados para
# o algoritmo de aprendizado de máquina escolhido e, realize novas simulações.

# 7) Gerar um relatório em formato (.PDF) contendo no mínimo:
    # o Resumo e imagem do fluxo de todas as etapas realizadas
    # o explicação das etapas realizadas (O que foi feito? Como foi feito?)
    # ⏲️ o gráfico de linha da série temporal total avaliada
    # ⏲️ o gráfico de barras contendo a percentual das classes calculadas
    # ⏲️ o quantitativo em percentual das classes calculadas
    # ⏲️ o quantidade de acertos e erros de previsão
    # ⏲️ o medidas de avaliação (acurácia, precisao, f1-score e especificidade)
    # ⏲️ o retorno financeiro das perdas em percentual
    # ⏲️ o retorno financeiro dos ganhos em percentual
    # ⏲️ o retorno financeiro geral (ganhos menos as perdas) em percentual
    # o conclusão sobre os resultados apresentados e o comportamento apresentado pelo seu algoritmo de aprendizado de máquina escolhido.

# 8) Criar um Dashboard para iniciar a aplicação e apresentação dos resultados
# solicitados no item 7.

# 9) Criar um filtro para selecionar o período de dados de Treinamento por ano.

# 10) Gravar um vídeo de no máximo 10 minutos mostrando código funcionando e
# explicando todo o trabalho realizado
    # O que deverá ser enviado?
    #  relatório em formato (.PDF)
    #  código implementado
    #  vídeo explicativo
    #  arquivo de cotações histórica (treinamento e Teste) utilizados