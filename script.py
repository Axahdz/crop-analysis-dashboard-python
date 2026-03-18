# =====================================================
# MULTI-PLANT ANALYSIS (Python Version)
# =====================================================

import pandas as pd
import os

# ---------------- CONFIG ----------------
base_path = os.path.dirname(__file__)
excel_path = os.path.join(base_path, "reportes_excel")

os.makedirs(excel_path, exist_ok=True)

files = ["planta_alpha.csv", "planta_beta.csv", "planta_gamma.csv"]

# ---------------- PROCESS ----------------
for file in files:
    plant_name = file.replace(".csv", "")
    print(f"\nProcessing {plant_name}...")

    df = pd.read_csv(f"data/{file}")

    # Combo column
    df["Combo"] = df["Variedad"] + " - " + df["Tipo"] + " - " + df["Region"]

    # Group by
    G = df.groupby("Combo").mean(numeric_only=True).reset_index()

    # ---------------- SORTINGS ----------------
    G_verde = G.sort_values("Verde", ascending=False)
    G_dt = G.sort_values("DT", ascending=False)
    G_dseco = G.sort_values("D_seco", ascending=False)
    G_solidos = G.sort_values("Solidos", ascending=False)
    G_rechazo = G.sort_values("Rechazo", ascending=False)
    G_varianza = G.sort_values("Varianza", ascending=False)
    G_descuento = G.sort_values("Descuento", ascending=False)
    G_rendimiento = G.sort_values("Rendimiento", ascending=False)

    # ---------------- EXPORT EXCEL ----------------
    def export_excel(df, filename, column_name):
        filepath = os.path.join(excel_path, filename)
        df[["Combo", column_name]].to_excel(filepath, index=False)

    export_excel(G_rendimiento, f"Reporte_Rendimiento_{plant_name}.xlsx", "Rendimiento")
    export_excel(G_dt, f"Reporte_DT_{plant_name}.xlsx", "DT")
    export_excel(G_dseco, f"Reporte_DSeco_{plant_name}.xlsx", "D_seco")
    export_excel(G_solidos, f"Reporte_Solidos_{plant_name}.xlsx", "Solidos")
    export_excel(G_rechazo, f"Reporte_Rechazo_{plant_name}.xlsx", "Rechazo")
    export_excel(G_varianza, f"Reporte_Varianza_{plant_name}.xlsx", "Varianza")
    export_excel(G_descuento, f"Reporte_Descuento_{plant_name}.xlsx", "Descuento")

    print(f"Excel reports generated for {plant_name}")