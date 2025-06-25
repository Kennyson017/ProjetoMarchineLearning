import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from datetime import datetime
import main


# Configurações da pagina
st.set_page_config(
    page_title="⚡Medium de Ações",
    page_icon="💲",
    layout="wide",
    initial_sidebar_state="expanded")

sidebar = True

# Style CSS
# with open('style.css', 'r') as fp:
#     st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)

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

    st.sidebar.button("Aplicar Filtros")

    return train_selected_years


render_sidebar()
