import streamlit as st
from checker import SecurityHeaderChecker
import json
import os

st.set_page_config(page_title="Validador de Vulnerabilidades", layout="centered")

st.title("🔒 Validador de Vulnerabilidades em Sites")
st.markdown("Este aplicativo verifica cabeçalhos de segurança e validade do certificado SSL de um site.")

url = st.text_input("Digite a URL (ex: https://exemplo.com):")

if st.button("Validar Site"):
    if not url.startswith("http"):
        st.warning("A URL deve começar com http:// ou https://")
    else:
        checker = SecurityHeaderChecker(url)

        with st.spinner("Analisando site..."):
            checker.analisar()
            resultado = checker.resultado

        st.success("Análise concluída!")

        st.subheader("Resultados da Validação:")
        for chave, valor in resultado.items():
            if isinstance(valor, dict):
                st.write(f"🔍 **{chave}**:")
                st.json(valor)
            else:
                st.write(f"**{chave}**: {valor}")

        if os.path.exists("relatorio.txt"):
            with open("relatorio.txt", "r", encoding="utf-8") as f:
                st.download_button("📄 Baixar Relatório TXT", f, file_name="relatorio.txt")

        if os.path.exists("relatorio.json"):
            with open("relatorio.json", "r", encoding="utf-8") as f:
                st.download_button("📄 Baixar Relatório JSON", f, file_name="relatorio.json")
