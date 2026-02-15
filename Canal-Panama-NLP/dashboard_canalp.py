import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Canal Panama Intel", layout="wide")
st.title("🚢 Dashboard de Inteligencia: Conflicto Canal de Panamá 2026")
st.markdown("---")

# Carga de datos
path_json = "output_json/"
all_triples = []

if os.path.exists(path_json):
    for file in os.listdir(path_json):
        if file.endswith(".json"):
            with open(os.path.join(path_json, file), 'r', encoding='utf-8') as f:
                data = json.load(f)
                for sentence in data['sentences']:
                    for triple in sentence.get('openie', []):
                        all_triples.append({
                            "Noticia": file.replace(".txt.json", ""),
                            "Sujeto": triple['subject'],
                            "Relación": triple['relation'],
                            "Objeto": triple['object'],
                            "Confianza": 1.0 # CoreNLP OpenIE default
                        })

df = pd.DataFrame(all_triples)

# SIDEBAR: Filtros para toma de decisiones
st.sidebar.header("🔍 Filtros Estratégicos")
actor_filter = st.sidebar.multiselect("Filtrar por Actor Principal:", options=df['Sujeto'].unique())
if actor_filter:
    df = df[df['Sujeto'].isin(actor_filter)]

# COLUMNAS DE MÉTRICAS
col1, col2, col3 = st.columns(3)
col1.metric("Hechos Extraídos", len(df))
col2.metric("Actores Identificados", df['Sujeto'].nunique())
col3.metric("Fuentes Procesadas", 5)

# VISUALIZACIÓN 1: Análisis de Frecuencia de Actores
st.subheader("📊 Volumen de Actividad por Actor")
fig_actors = px.bar(df['Sujeto'].value_counts().head(10), labels={'value':'Frecuencia', 'index':'Actor'}, color_discrete_sequence=['#00ffcc'])
st.plotly_chart(fig_actors, use_container_width=True)

# VISUALIZACIÓN 2: Matriz de Hechos (La parte "Cool")
st.subheader("📑 Base de Conocimiento Estructurada")
st.dataframe(df, use_container_width=True)

# SECCIÓN DE ANÁLISIS PARA TOMA DE DECISIONES
st.markdown("---")
st.header("🧠 Análisis para la Toma de Decisiones")
col_a, col_b = st.columns(2)

with col_a:
    st.info("**Análisis de Riesgo:**")
    threats = df[df['Relación'].str.contains('threaten|invalidated|limit', case=False)]
    st.write(f"Se han detectado **{len(threats)}** acciones de riesgo directo a la soberanía.")
    st.table(threats[['Sujeto', 'Relación', 'Objeto']].head())

with col_b:
    st.success("**Análisis de Estabilidad:**")
    stability = df[df['Relación'].str.contains('defend|sovereignty|treaty', case=False)]
    st.write(f"Se han detectado **{len(stability)}** acciones de refuerzo diplomático.")
    st.table(stability[['Sujeto', 'Relación', 'Objeto']].head())