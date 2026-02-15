import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Canal Panama Intel", layout="wide")
st.title("🚢 Dashboard de Inteligencia: Conflicto Canal de Panamá 2026")
st.markdown("---")

# --- CORRECCIÓN DE RUTA (SOLUCIONA EL KEYERROR) ---
# Esto busca la carpeta 'output_json' relativa a la ubicación del script
current_dir = os.path.dirname(__file__)
path_json = os.path.join(current_dir, "output_json")

all_triples = []

# Carga de datos con verificación
if os.path.exists(path_json):
    files = [f for f in os.listdir(path_json) if f.endswith(".json")]
    for file in files:
        with open(os.path.join(path_json, file), 'r', encoding='utf-8') as f:
            data = json.load(f)
            for sentence in data.get('sentences', []):
                for triple in sentence.get('openie', []):
                    all_triples.append({
                        "Noticia": file.replace(".txt.json", ""),
                        "Sujeto": triple['subject'],
                        "Relación": triple['relation'],
                        "Objeto": triple['object']
                    })
else:
    st.error(f"Error Crítico: No se encontró la carpeta de datos en {path_json}")

# --- VALIDACIÓN DE DATOS ---
if not all_triples:
    st.warning("⚠️ El sistema no ha detectado hechos procesados. Verifica que los archivos JSON estén en la carpeta correcta.")
    st.stop() # Detiene la ejecución de forma limpia si no hay datos

df = pd.DataFrame(all_triples)

# Filtros Estratégicos
st.sidebar.header("🔍 Filtros Estratégicos")
actor_filter = st.sidebar.multiselect("Filtrar por Actor Principal:", options=df['Sujeto'].unique())
if actor_filter:
    df = df[df['Sujeto'].isin(actor_filter)]

# Métricas Principales
col1, col2, col3 = st.columns(3)
col1.metric("Hechos Extraídos", len(df))
col2.metric("Actores Identificados", df['Sujeto'].nunique())
col3.metric("Fuentes Procesadas", 5)

# Gráfico de Barras
st.subheader("📊 Volumen de Actividad por Actor")
fig_actors = px.bar(df['Sujeto'].value_counts().head(10), labels={'value':'Frecuencia', 'index':'Actor'}, color_discrete_sequence=['#00ffcc'])
st.plotly_chart(fig_actors, use_container_width=True)

# Tabla de Datos
st.subheader("📑 Base de Conocimiento Estructurada")
st.dataframe(df, use_container_width=True)
