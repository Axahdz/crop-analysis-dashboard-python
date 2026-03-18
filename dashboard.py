import streamlit as st
import pandas as pd

st.title("🌱 Agricultural Dashboard")

# Upload file
file = st.file_uploader("Upload CSV", type="csv")

if file:
    df = pd.read_csv(file)

    df["Combo"] = df["Variedad"] + " - " + df["Tipo"] + " - " + df["Region"]
    G = df.groupby("Combo").mean(numeric_only=True).reset_index()

    metric = st.selectbox("Select Metric", [
        "Rendimiento", "DT", "D_seco",
        "Solidos", "Rechazo", "Varianza", "Descuento"
    ])

    G_sorted = G.sort_values(metric, ascending=False)

    st.subheader(f"{metric} Ranking")
    st.bar_chart(G_sorted.set_index("Combo")[metric])

    # KPIs
    st.metric("Max", round(G[metric].max(),2))
    st.metric("Min", round(G[metric].min(),2))
    st.metric("Mean", round(G[metric].mean(),2))