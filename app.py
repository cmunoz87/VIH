import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Flujo de Interpretación VIH", layout="centered")
st.title("🧬 Flujo de Interpretación de Resultados VIH")

# Botón para reiniciar flujo
if st.button("🔄 Reiniciar flujo"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()

# Diagrama del flujo
st.markdown("""
### 📌 Diagrama del flujo de una muestra VIH:
1️⃣ **Resultado inicial cuantitativo**  
⬇️  
2️⃣ **Si < 1 → No reactivo → Emitir informe**  
⬇️  
3️⃣ **Si ≥ 1 → Repetición 1 y 2**  
⬇️  
4️⃣ **Ambas < 1 → No reactivo → Emitir informe**  
⬇️  
5️⃣ **Una o ambas ≥ 1 → Reactivo → Confirmación ISP**  
⬇️  
6️⃣ **ISP negativo → Emitir informe**  
⬇️  
7️⃣ **ISP positivo → Prueba de identidad**  
⬇️  
8️⃣ **Prueba identidad < 1 → No reactivo → Revisar proceso**  
⬇️  
9️⃣ **Prueba identidad ≥ 1 → Reactivo → Confirmar diagnóstico**
""")

st.divider()
st.write("Ingrese el resultado inicial para iniciar el flujo de interpretación.")

# Paso 1: Resultado cuantitativo inicial
resultado_inicial = st.number_input("Resultado cuantitativo inicial", min_value=0.0, step=0.01, key="resultado_inicial")

if resultado_inicial < 1:
    st.success("Resultado cuantitativo: NO REACTIVO ✅. SE EMITE INFORME.")
else:
    st.warning("Resultado inicial REACTIVO ⚠️. Ingrese las repeticiones:")

    # Paso 2: Repeticiones
    repeticion1 = st.number_input("Repetición 1", min_value=0.0, step=0.01, key="repeticion1")
    repeticion2 = st.number_input("Repetición 2", min_value=0.0, step=0.01, key="repeticion2")

    # Evaluación de repeticiones
    if repeticion1 > 0 or repeticion2 > 0:
        if repeticion1 < 1 and repeticion2 < 1:
            st.success("Resultado cualitativo: NO REACTIVO ✅. SE EMITE INFORME.")
        else:
            st.error("Resultado cualitativo: REACTIVO ⚠️")
            st.info("Se requiere confirmación ISP")

            # Paso 3: Confirmación ISP
            confirmacion_isp = st.selectbox(
                "Resultado confirmación ISP",
                ["Seleccionar", "Negativo", "Positivo"],
                key="confirmacion_isp"
            )

            if confirmacion_isp == "Negativo":
                st.success("Confirmación ISP: NEGATIVO ✅. SE EMITE INFORME.")
            elif confirmacion_isp == "Positivo":
                st.warning("Confirmación ISP: POSITIVO ⚠️. Requiere prueba de identidad.")

                # Paso 4: Prueba de identidad
                prueba_identidad = st.number_input("Resultado prueba de identidad", min_value=0.0, step=0.01, key="prueba_identidad")

                if prueba_identidad > 0:
                    if prueba_identidad < 1:
                        st.warning("Resultado prueba de identidad: NO REACTIVO ⚠️. Revisar todo el proceso, no  emitir informe.")
                    else:
                        st.error("Resultado prueba de identidad: REACTIVO 🔴. emitir informe.")

