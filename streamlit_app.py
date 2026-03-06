import streamlit as st

# Configuración visual
st.set_page_config(page_title="Progressive FCR Bot", layout="centered")

# Estilo de "Chat/Bot"
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        background-color: #262730;
        color: #ffffff;
        border: 2px solid #00529b;
        font-size: 20px !important;
    }
    .bot-response {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00529b;
        margin-top: 20px;
    }
    .highlight { color: #ffcc00; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 FCR Interactive Bot")
st.write("Escribe tu caso (ej: 'add vehicle', 'claims', 'pago fallido')")

# --- LÓGICA DEL BOT ---
user_input = st.text_input("¿Qué necesita el cliente?", placeholder="Escribe aquí...").lower()

if user_input:
    st.markdown("---")
    
    # CASO: ADD VEHICLE
    if "add" in user_input or "vehicle" in user_input or "vehiculo" in user_input:
        st.markdown(f"""
        <div class="bot-response">
            <h3>🚗 Add/Update Vehicle Kit</h3>
            <p><b>Script Empático:</b> "Claro que sí, Felipe. Felicidades por el nuevo vehículo, con gusto lo protegemos hoy mismo en su póliza."</p>
            <p><b>Hack de FCR:</b> No olvides mencionar que recibirá su <b>ID Card digital</b> en la App OLS de inmediato.</p>
            <p><b>Evita la rellamada:</b> Confirma si el vehículo reemplaza a otro para evitar cobros dobles que generarían una queja mañana.</p>
        </div>
        """, unsafe_allow_html=True)

    # CASO: CLAIMS / RECLAMOS
    elif "claim" in user_input or "reclamo" in user_input or "choque" in user_input:
        st.markdown(f"""
        <div class="bot-response">
            <h3>📞 Protocolo de Reclamos (Ext 425)</h3>
            <p><b>Script Empático:</b> "Lamento mucho el incidente. Mi prioridad es conectarlo con el experto que lleva su caso para que no pierda tiempo."</p>
            <p><b>Instrucciones:</b> Canalizar a la <b>Ext 425</b>. Número directo: <b>800-274-4499</b>.</p>
            <p><b>Hack de FCR:</b> Invítalo a usar la <b>App OLS</b> para ver el nombre de su ajustador y fotos del reclamo en tiempo real.</p>
        </div>
        """, unsafe_allow_html=True)

    # CASO: PAGOS / BILLING
    elif "pago" in user_input or "billing" in user_input or "money" in user_input:
        st.markdown(f"""
        <div class="bot-response">
            <h3>💵 Billing & Payments</h3>
            <p><b>Script Empático:</b> "Entiendo la importancia de mantener su cobertura activa. Revisemos juntos su estado de cuenta."</p>
            <p><b>Hack de FCR:</b> Si hubo un pago devuelto, advierte sobre el cargo de $25 de Progressive para que no llame a reclamarlo después.</p>
            <p><b>Digital Tool:</b> Sugiere activar el <b>AutoPay</b> para evitar olvidos.</p>
        </div>
        """, unsafe_allow_html=True)

    # CASO: CANCELACIONES
    elif "cancel" in user_input:
        st.markdown(f"""
        <div class="bot-response">
            <h3>🛑 Retención / Cancelación</h3>
            <p><b>Regla de Oro:</b> Si es de Agencia, referir al agente <b>2 VECES</b> (salvo alerta 'No refer').</p>
            <p><b>Hack de FCR:</b> Si cancela por venta, ofrece <b>Non-Owner</b> para que su historial no se vea afectado por falta de cobertura.</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.info("No reconozco ese comando todavía. Prueba con 'add vehicle', 'claims' o 'pagos'.")

# --- PIE DE PÁGINA ---
st.sidebar.markdown("### ⚡ Comandos Rápidos")
st.sidebar.write("- `add vehicle`")
st.sidebar.write("- `claims`")
st.sidebar.write("- `pagos`")
st.sidebar.write("- `cancelar`")
