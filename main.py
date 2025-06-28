import modulos.functions as mf
from modulos.algoritmos import DecisionTree, simular_retorno_financeiro
import modulos.config as mc
import streamlit as st
import pandas as pd
import modulos.interface as mi

# Configurações da pagina
st.set_page_config(
    page_title="⚡Medium de Ações",
    page_icon="💲",
    layout="wide",
    initial_sidebar_state="expanded")

selected_ticker, train_selected_years,  test_selected_year, show_train = mi.render_sidebar()

mc.ticker = f"{selected_ticker}.SA"

mf.create_csv()

df = mf.treat_csv()

train = df[df['Date'].dt.year.isin(train_selected_years)]
test_year = test_selected_year
test = df[df['Date'].dt.year == test_year]

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

# print("\nDECISION TREE ----------------\n")
result_dt = DecisionTree(x_train, y_train, y_test, x_test, test)
retorno = simular_retorno_financeiro(test, result_dt['y_pred'], investimento_por_trade=1000)
# print("\nRamdom Forest ----------------\n")
# RamdomForest(x_train, y_train, y_test, x_test)

mi.render_metrics_dashboard(
    recall = result_dt['recall'],
    hits = result_dt['hits'],
    misses = result_dt['misses'],
    accuracy = result_dt['accuracy'],
    precision = result_dt['precision'],
    f1_score = result_dt['f1_score'],
    specificity = result_dt['specificity'],
    loss_return = result_dt['loss_return'],
    gain_return = result_dt['gain_return'],
    net_return = result_dt['net_return']
)

# mi.render_metrics_dashboard(
#     recall = result_dt['class_percent'],
#     hits = result_dt['hits'],
#     misses = result_dt['misses'],
#     accuracy = result_dt['accuracy'],
#     precision = result_dt['precision'],
#     f1_score = result_dt['f1_score'],
#     specificity = result_dt['specificity'],
#     loss_return = retorno['loss_return'],
#     gain_return = retorno['gain_return'],
#     net_return = retorno['retorno_percentual']
# )


col1, col2 = st.columns([3,1])

with col1:

    # mi.plot_time_series(test, "Date", "Close", "📈 Evolução do Indicador")

    test['y_pred'] = result_dt['y_pred']
    test['Acerto'] = test['y_pred'] == test['Target']
    test['Cor'] = test['Acerto'].map({True: 'green', False: 'red'})
    test['Fase'] = 'Teste'

    train['Fase'] = 'Treino'
    train['Cor'] = None  # Sem marcação de acerto/erro no treino

    mi.plot_scatter(test, train if show_train else None)
    

with col2:
    labels_map = {1: "Alta", 0: "Baixa"}
    class_counts = test['Target'].map(labels_map).value_counts(normalize=True) * 100
    class_distribution = class_counts.to_dict()

    mi.plot_class_distribution(class_distribution)












# Style CSS
# with open('style.css', 'r') as fp:
#     st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)








# print("Período de treino:", train['Date'].min(), "->", train['Date'].max())
# print("Período de teste:", test['Date'].min(), "->", test['Date'].max())


# 👍1) Escolher um código de ativo da B3 e Baixar 3 anos (2023, 2024 e 2025) de
# dados de cotação histórica do ativo escolhido de granularidade (período) diária.


# 👍2) Para o período selecionado, calcular o atributo alvo através da diferença entre o Peço de Abertura e o Preço de Fechamento. Caso o resultado seja positivo o novo atributo alvo terá o valor de 1. E caso o contrário, o novo atributo alvo terá o valor de 0.

# 👍3) Separar os dados em Treinamento (2023 e 2024) e Teste (2025)

# 👍4) Escolher na biblioteca sci-kit learn e implementar um algoritmo de aprendizado de máquina categoria supervisionado (classificador) (KNN, DT, NB, SVM e outro).

# 👍5) Realizar as simulações e ajustar os parâmetros do algoritmo escolhido aos
# dados avaliados.

# 👍6) Revisar os dados coletados com o objetivo de retirar ruídos e ou atributos
# irrelevantes e, em seguida, proponha uma nova forma de treinar os dados para
# o algoritmo de aprendizado de máquina escolhido e, realize novas simulações.

# 7) Gerar um relatório em formato (.PDF) contendo no mínimo:
    # o Resumo e imagem do fluxo de todas as etapas realizadas
    # 👍 o explicação das etapas realizadas (O que foi feito? Como foi feito?)
    # 👍 o gráfico de linha da série temporal total avaliada
    # 👍 o gráfico de barras contendo a percentual das classes calculadas
    # 👍 o quantitativo em percentual das classes calculadas
    # 👍 o quantidade de acertos e erros de previsão
    # 👍 o medidas de avaliação (acurácia, precisao, f1-score e especificidade)
    # 👍 o retorno financeiro das perdas em percentual
    # 👍 o retorno financeiro dos ganhos em percentual
    # 👍 o retorno financeiro geral (ganhos menos as perdas) em percentual
    # o conclusão sobre os resultados apresentados e o comportamento apresentado pelo seu algoritmo de aprendizado de máquina escolhido.

# 👍8) Criar um Dashboard para iniciar a aplicação e apresentação dos resultados
# solicitados no item 7.

# 👍9) Criar um filtro para selecionar o período de dados de Treinamento por ano.

# 10) Gravar um vídeo de no máximo 10 minutos mostrando código funcionando e
# explicando todo o trabalho realizado
    # O que deverá ser enviado?
    #  relatório em formato (.PDF)
    #  código implementado
    #  vídeo explicativo
    #  arquivo de cotações histórica (treinamento e Teste) utilizados