import modulos.functions as mf
from sklearn import tree 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = mf.treat_csv()

# train = df[(df['Date'].dt.year >= 2023) & (df['Date'].dt.year <= 2024)]
train = df[(df['Date'].dt.year <= 2024)]
test = df[(df['Date'].dt.year == 2025)]

# print("Período de treino:", train['Date'].min(), "->", train['Date'].max())
# print("Período de teste:", test['Date'].min(), "->", test['Date'].max())

# TREINAMENTO

# Features e Targets dos dataframes
features = ['Open', 'High', 'Low', 'Close', 'Volume']
target = 'Target'

# Treino
X_train = train[features] # features
y_train = train[target] # target

# Teste 
x_test = test[features]
y_teste = test[target]

def DesionTree():
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    y_pred = clf.predict(x_test)

    print("Acurácia:", accuracy_score(y_teste, y_pred))
    print("\nRelatório de Classificação:\n", classification_report(y_teste, y_pred))
    print("\nMatriz de Confusão:\n", confusion_matrix(y_teste, y_pred))





















# 👍1) Escolher um código de ativo da B3 e Baixar 3 anos (2023, 2024 e 2025) de
# dados de cotação histórica do ativo escolhido de granularidade (período) diária.


# 👍2) Para o período selecionado, calcular o atributo alvo através da diferença entre o Peço de Abertura e o Preço de Fechamento. Caso o resultado seja positivo o novo atributo alvo terá o valor de 1. E caso o contrário, o novo atributo alvo terá o valor de 0.

# 👍3) Separar os dados em Treinamento (2023 e 2024) e Teste (2025)

# 4) Escolher na biblioteca sci-kit learn e implementar um algoritmo de aprendizado de máquina categoria supervisionado (classificador) (KNN, DT, NB, SVM e outro).

# 5) Realizar as simulações e ajustar os parâmetros do algoritmo escolhido aos
# dados avaliados.

# 6) Revisar os dados coletados com o objetivo de retirar ruídos e ou atributos
# irrelevantes e, em seguida, proponha uma nova forma de treinar os dados para
# o algoritmo de aprendizado de máquina escolhido e, realize novas simulações.

# 7) Gerar um relatório em formato (.PDF) contendo no mínimo:
    # o Resumo e imagem do fluxo de todas as etapas realizadas
    # o explicação das etapas realizadas (O que foi feito? Como foi feito?)
    # o gráfico de linha da série temporal total avaliada
    # o gráfico de barras contendo a percentual das classes calculadas
    # o quantitativo em percentual das classes calculadas
    # o quantidade de acertos e erros de previsão
    # o medidas de avaliação (acurácia, precisao, f1-score e especificidade)
    # o retorno financeiro das perdas em percentual
    # o retorno financeiro dos ganhos em percentual
    # o retorno financeiro geral (ganhos menos as perdas) em percentual
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