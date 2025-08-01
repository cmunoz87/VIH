import streamlit as st

# Configuración general
st.set_page_config(page_title="Flujo de Resultados VIH", layout="centered")
st.title("🧬 Flujo de Interpretación de Resultados VIH")

# Inicializar estado
if "reiniciar" not in st.session_state:
    st.session_state.reiniciar = False

# Botón de reinicio
if st.button("🔄 Reiniciar flujo"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()

# Diagrama visual
st.markdown("""
### 📌 Diagrama del flujo de una muestra VIH:
1️⃣ **Resultado inicial cuantitativo**  
⬇️  
2️⃣ **Si < 1 → No reactivo → Emitir informe**  
⬇️  
3️⃣ **Si ≥ 1 → Repetir prueba (Repetición 1 y 2)**  
⬇️  
4️⃣ **Ambas < 1 → No reactivo → Emitir informe**  
⬇️  
5️⃣ **Una o ambas ≥ 1 → Reactivo → Confirmación ISP**  
⬇️  
6️⃣ **ISP negativo → Emitir informe**  
⬇️  
7️⃣ **ISP positivo → Prueba de identidad**  
⬇️  
8️⃣ **Prueba identidad < 1 → No reactivo / ≥ 1 → Reactivo**
""")

st.divider()
st.write("Ingrese el resultado inicial para iniciar el flujo de interpretación.")

# Paso 1: Resultado cuantitativo 
