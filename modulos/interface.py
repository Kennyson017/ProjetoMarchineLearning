import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def render_sidebar():
    st.sidebar.title('💲Monitor de Ações')
    st.sidebar.markdown("### Filtros")

    selected_ticker = st.sidebar.selectbox("Escolha a ação", ["PETR4", "VALE3", "ITUB4", "BBAS3", "MGLU3"])

    current_year = datetime.now().year
    years = list(range(2020, current_year + 1))

    train_selected_years = st.sidebar.multiselect(
        "Selecione o periodo de Treinamento",
        options=years,
        default=[2023, 2024]
    )

    if len(train_selected_years) < 2:
        st.sidebar.warning("Selecione pelo menos 2 anos para o treinamento.")

    test_selected_year = st.sidebar.selectbox(
        "Selecione o periodo de Teste",
        options=years,
        index=years.index(2025) if 2025 in years else 0
    )

    if train_selected_years and test_selected_year <= max(train_selected_years):
        st.sidebar.error(
            f"O ano de teste ({test_selected_year}) deve ser posterior ao último ano de treino ({max(train_selected_years)})."
        )
        st.stop()

    show_train = st.sidebar.toggle("Mostrar período de treinamento no gráfico", value=True)

    return selected_ticker, train_selected_years, test_selected_year, show_train

def render_metrics_dashboard(
    recall, hits, misses,
    accuracy, precision, f1_score, specificity,
    loss_return, gain_return, net_return
):
    st.markdown("### 📊 Desempenho do Modelo")

    # Primeira linha: distribuição e desempenho do modelo
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("🎯 Recall", f"{recall:.2f}")
    col2.metric("✅ Acertos", f"{hits}")
    col3.metric("❌ Erros", f"{misses}")
    col4.metric("📈 Acurácia", f"{accuracy:.2%}")
    col5.metric("🔍 Precisão", f"{precision:.2%}")

    # Segunda linha: métricas complementares e retorno financeiro
    col6, col7, col8, col9, col10 = st.columns(5)
    col6.metric("📊 F1-score", f"{f1_score:.2%}")
    col7.metric("🧪 Especificidade", f"{specificity:.2%}")
    col8.metric("📉 Perdas (%)", f"{loss_return:.2f}%", delta=loss_return)
    col9.metric("📈 Ganhos (%)", f"{gain_return:.2f}%", delta=gain_return)
    col10.metric("💰 Retorno Líquido", f"{net_return:.2f}%", delta=net_return)

def plot_time_series(data: pd.DataFrame, date_col: str, value_col: str, title: str = "📈 Série Temporal"):
    fig = px.line(
        data,
        x=date_col,
        y=value_col,
        title=title,
        markers=True,
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_time_series_multiple(data: pd.DataFrame, date_col: str, value_cols: list, title: str = "📈 Série Temporal"):
    df_melt = data.melt(id_vars=[date_col], value_vars=value_cols,
                        var_name="Série", value_name="Valor")

    fig = px.line(
        df_melt,
        x=date_col,
        y="Valor",
        color="Série",
        title=title,
        markers=True,
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

def plot_class_distribution(class_counts: dict, title: str = "📊 Distribuição das Classes"):
    df_classes = pd.DataFrame({
        "Classe": list(class_counts.keys()),
        "Percentual": [v for v in class_counts.values()]
    })

    color_map = {
        "Alta": "green",
        "Baixa": "red",
        "Estável": "gray"  # opcional
    }

    fig = px.bar(
        df_classes,
        x="Classe",
        y="Percentual",
        text="Percentual",
        title=title,
        template="plotly_white",
        color="Classe",
        color_discrete_map=color_map
    )

    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig.update_layout(yaxis_ticksuffix="%", yaxis_range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)

# def plot_scatter(test):

#     fig = px.scatter(
#     test,
#     x='Date',
#     y='Close',
#     color='Cor',
#     color_discrete_map={'green': 'green', 'red': 'red'},
#     title='📈 Preço Real com Marcação dos Acertos e Erros',
#     labels={'Close': 'Preço de Fechamento'},
#     opacity=0.8
# )

#     # Adiciona linha do preço real
#     fig.add_trace(
#         go.Scatter(
#             x=test['Date'],
#             y=test['Close'],
#             mode='lines',
#             name='Preço Real',
#             line=dict(color='gray')
#         )
#     )

#     st.plotly_chart(fig, use_container_width=True)

def plot_scatter(test_df, train_df=None ):

    if train_df is not None:
        df = pd.concat([train_df, test_df])
    else:
        df = test_df.copy()

    fig = px.scatter(
        test_df if test_df is not None else pd.DataFrame(columns=["Date", "Close", "Cor"]),
        x='Date',
        y='Close',
        color='Cor',
        color_discrete_map={'green': 'green', 'red': 'red'},
        title='📈 Linha de Serie Temporal com Marcação de Acertos e Erros',
        labels={'Close': 'Preço de Fechamento'},
        opacity=0.8
    )

    fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['Close'],
            mode='lines',
            name='Preço Real',
            line=dict(color='gray', width=2)
        )
    )

    st.plotly_chart(fig, use_container_width=True)