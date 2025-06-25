import streamlit as st
import pandas as pd
import modulos.interface as mi

# Configurações da pagina
st.set_page_config(
    page_title="⚡Medium de Ações",
    page_icon="💲",
    layout="wide",
    initial_sidebar_state="expanded")

# sidebar = True

mi.render_sidebar()

mi.render_metrics_dashboard(
    class_percent=66.7,
    hits=120,
    misses=30,
    accuracy=0.80,
    precision=0.75,
    f1_score=0.77,
    specificity=0.85,
    loss_return=4.2,
    gain_return=7.5,
    net_return=3.3
)

col1, col2 = st.columns(2)

with col1:
    # Simulando uma série temporal
    dates = pd.date_range(start="2023-01-01", periods=12, freq="M")
    values = [100 + i * 5 + (i % 3) * 10 for i in range(12)]
    df_series = pd.DataFrame({"Data": dates, "Valor": values})

    mi.plot_time_series(df_series, "Data", "Valor", "📈 Evolução do Indicador")

with col2:
    # Simulando as classes
    class_distribution = {
        "Alta": 45.0,
        "Baixa": 35.0,
        "Estável": 20.0
    }

    mi.plot_class_distribution(class_distribution)












# Style CSS
# with open('style.css', 'r') as fp:
#     st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)