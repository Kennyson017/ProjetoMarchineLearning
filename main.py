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

result_dt = DecisionTree(x_train, y_train, y_test, x_test, test)
retorno = simular_retorno_financeiro(test, result_dt['y_pred'], investimento_por_trade=1000)


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


col1, col2 = st.columns([3,1])

with col1:

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