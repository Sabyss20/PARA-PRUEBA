import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Agenda de Reunión", layout="wide")

st.title("📅 Agenda de Reunión")

# Datos de ejemplo (predefinidos en el código)
data = {
    "Hora de inicio": ["09:00", "09:30", "10:00", "10:30"],
    "Hora de fin": ["09:30", "10:00", "10:30", "11:00"],
    "Tema": ["Bienvenida", "Revisión de avances", "Discusión de metas", "Cierre"],
    "Encargado": ["Ana", "Luis", "María", "Carlos"],
}
df = pd.DataFrame(data)

# Mostrar tabla
st.subheader("🧾 Detalle de la agenda")
st.table(df)

# Gráfico tipo Gantt con Altair (opcional)
st.subheader("📊 Visualización de tiempos")

chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x="Hora de inicio",
        x2="Hora de fin",
        y="Tema",
        color="Encargado",
        tooltip=["Tema", "Encargado", "Hora de inicio", "Hora de fin"],
    )
    .properties(height=300)
)

st.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.caption("App creada con 💚 Streamlit")

