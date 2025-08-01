import streamlit as st

# Configuración general
st.set_page_config(page_title="Flujo de Resultados VIH", layout="centered")
st.title("🧬 Flujo de Interpretación de Resultados VIH")

# Inicializar estado
if "reiniciar" not in st.session_state:
    st.session_state.reiniciar = False

# Botón de reinicio
if st.button("🔄 Reiniciar flujo"):
    st.session_state.reiniciar = True
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

# Paso 1: Resultado cuantitativo inicial
resultado_inicial = st.number_input("Resultado cuantitativo inicial", min_value=0.0, step=0.01, key="resultado_inicial")

if resultado_inicial < 1:
    st.success("Resultado cuantitativo: NO REACTIVO. ✅ SE EMITE INFORME.")
else:
    st.warning("Resultado inicial REACTIVO. Ingrese las repeticiones:")

    # Paso 2: Repeticiones
    repeticion1 = st.number_input("Repetición 1", min_value=0.0, step=0.01, key="repeticion1")
    repeticion2 = st.number_input("Repetición 2", min_value=0.0, step=0.01, key="repeticion2")

    if st.button("Evaluar repeticiones"):
        if repeticion1 < 1 and repeticion2 < 1:
            st.success("Resultado cualitativo: NO REACTIVO ✅")
        else:
            st.error("Resultado cualitativo: REACTIVO ⚠️")
            st.info("Se requiere confirmación ISP")

            # Paso 3: Confirmación ISP
            confirmacion_isp = st.selectbox("Resultado confirmación ISP", ["Seleccionar", "Negativo", "Positivo"], key="confirmacion_isp")

            if confirmacion_isp == "Negativo":
                st.success("Confirmación ISP: NEGATIVO. ✅ EMITIR INFORME.")
            elif confirmacion_isp == "Positivo":
                st.warning("Confirmación ISP: POSITIVO. Requiere prueba de identidad.")

                # Paso 4: Prueba de identidad
                prueba_identidad = st.number_input("Resultado prueba de identidad", min_value=0.0, step=0.01, key="prueba_identidad")

                if prueba_identidad < 1:
                    st.success("Resultado prueba de identidad: NO REACTIVO ✅")
                else:
                    st.error("Resultado prueba de identidad: REACTIVO ⚠️")
