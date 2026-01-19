import streamlit as st
import pandas as pd
import json
import os

# Configuración de la página con un toque profesional
st.set_page_config(page_title="Perfil RRHH - Sergio Lérida", layout="wide")

st.title("📊 Visualizador de Perfil Profesional")
st.info("Cargando datos de: perfil_rrhh_sergio_lerida_toro_.json")

# Función para cargar el JSON específico
def load_data():
    file_name = 'perfil_rrhh_sergio_lerida_toro_.json'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        st.error(f"❌ No se encontró el archivo '{file_name}' en el repositorio.")
        return None

data = load_data()

if data:
    # Si el JSON es una lista de elementos, Pandas lo convierte en tabla automáticamente
    # Si es un solo objeto, lo metemos en una lista para que se vea bien
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    else:
        df = pd.DataFrame(data)

    # Mostrar los datos de forma organizada
    st.subheader("Información Extraída")
    st.dataframe(df, use_container_width=True)

    # Sidebar con utilidades
    st.sidebar.header("Opciones")
    if st.sidebar.button("Refrescar Datos"):
        st.rerun()
    
    # Botón para exportar a Excel/CSV, muy útil en Administración
    csv = df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
        label="📥 Descargar en CSV",
        data=csv,
        file_name='perfil_rrhh_export.csv',
        mime='text/csv',
          )
  
