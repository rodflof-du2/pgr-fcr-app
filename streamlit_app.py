import streamlit as st

st.set_page_config(page_title="Progressive CSR Lvl II - FCR Hub", layout="wide")

# CSS personalizado para que se vea modo oscuro/profesional
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #00529b; color: white; }
    .status-box { padding: 10px; border-radius: 5px; margin: 5px 0; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Progressive Lvl II: FCR Optimizer")
st.write("Felipe, usa este panel para cerrar llamadas sin que el cliente regrese.")

# --- BARRA LATERAL: RECURSOS RÁPIDOS ---
st.sidebar.header("☎️ Directorio Directo")
st.sidebar.error("**CLAIMS (Ext 425)**")
st.sidebar.code("800-274-4499")
st.sidebar.info("**Digital Tools**")
st.sidebar.write("- OLS App\n- Progressive.com")
st.sidebar.divider()
st.sidebar.warning("⚠️ **Agencias / Cancelaciones**")
st.sidebar.write("1. Referir al agente (Intento 1)")
st.sidebar.write("2. Referir al agente (Intento 2)")
st.sidebar.write("3. Si insiste: Cancelar (o ver alerta 'No refer')")

# --- CUERPO PRINCIPAL ---
tab1, tab2, tab3, tab4 = st.tabs(["💵 Pagos/Billing", "🚗 Cambios/Policy", "🛑 Cancelaciones", "📞 Transferencias/UW"])

with tab1:
    st.subheader("Resolución de Pagos (EFT/Billing)")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Pago Fallido / Devuelto"):
            st.warning("**Hack FCR:** Explica el cobro de $25 de Progressive + posible cargo del banco.")
            st.code("Script: 'Ya corregimos el método de pago. Para que no tenga que llamarnos de nuevo, le aviso que su banco podría generar un cargo administrativo por el intento fallido previo.'")
    with col2:
        if st.button("Aumento de Prima"):
            st.info("**Hack FCR:** No digas 'subió'. Di 'ajuste por zona/cobertura' y ofrece revisar descuentos.")

with tab2:
    st.subheader("Actualizaciones de Póliza")
    opc_poliza = st.selectbox("Tipo de Cambio:", ["Add/Remove Vehicle", "Update Driver", "Change Coverages", "Replace Auto"])
    if opc_poliza:
        st.success("**Hack FCR:** Informa sobre el ID Card digital inmediato.")
        st.write("Recuerda al cliente que puede ver su nueva ID Card en la **App OLS** ahora mismo sin esperar al correo postal.")

with tab3:
    st.subheader("Protocolo de Cancelación")
    st.error("¿Es de Agencia?")
    st.write("Verifica si hay alerta de **'DO NOT REFER'**. Si no la hay, debes re-direccionar al agente 2 veces antes de procesar.")
    st.info("**Tip FCR:** Si cancelan por venta, sugiere 'Non-Owner' para evitar el recargo por 'Lapse in Coverage' cuando compren otro auto.")

with tab4:
    st.subheader("Claims / Reclamos (Transferencia)")
    st.markdown("""
    <div class='status-box'>
    <b>Pasos para FCR en Reclamos:</b><br>
    1. NO des el número de reclamo (no estamos autorizados).<br>
    2. Da el número directo: <b>800-274-4499</b>.<br>
    3. Conecta a la <b>Ext. 425</b>.<br>
    4. Promociona <b>OLS App</b> para ver el estatus del reclamo y quién es su ajustador asignado.
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("Felipe, recuerda: Un cliente que sabe usar la App OLS es un cliente que no vuelve a llamar por estatus.")
