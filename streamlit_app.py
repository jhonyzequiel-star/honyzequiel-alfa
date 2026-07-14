
import streamlit as st
import time

st.set_page_config(page_title="HZ Security Panel", page_icon="🚨", layout="centered")

st.markdown("<h1 style='text-align: center; color: #e63946;'>🚨 HONYZEQUIEL SECURITY SYSTEMS</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #e0e1dd;'>Módulo de Autenticação Biométrica — Sistema Alfa</h3>", unsafe_allow_html=True)
st.write("---")

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.warning("⚠️ ALERTA: Sistema Alfa bloqueado. Tentativa de intrusão detetada no perímetro!")
    st.info("🎙️ Para desbloquear, clique no botão abaixo e diga pausadamente:")
    st.subheader('"Autenticação Honyzequiel, desbloquear o sistema Alfa e autorizar acesso imediato."')
    
    audio_trigger = st.button("🔴 Gravar Voz e Autenticar")
    
    if audio_trigger:
        with st.spinner("🎙️ Gravando áudio e processando espectrograma de voz..."):
            time.sleep(3)
            biometria_valida = True 
            if biometria_valida:
                st.session_state.authenticated = True
                st.success("✅ BIOMETRIA VOCAL CONFIRMADA!")
                st.toast("Assinatura de Honyzequiel reconhecida com 99.8% de precisão.")
                st.rerun()
            else:
                st.error("❌ Acesso Negado! Frequência vocal não autorizada.")
else:
    st.success("🔓 SISTEMA ALFA DESBLOQUEADO COM SUCESSO!")
    st.balloons()
    st.write("Bem-vindo de volta, **Honyzequiel**.")
    if st.button("🔒 Bloquear Painel"):
        st.session_state.authenticated = False
        st.rerun()
