import modulos.functions as mf

df = mf.treat_csv()

train = df[(df['Date'].dt.year >= 2023) & (df['Date'].dt.year <= 2024)]
test = df[(df['Date'].dt.year == 2025)]


mf.features_dataframe(df)