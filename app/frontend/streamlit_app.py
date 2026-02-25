import os
import streamlit as st
import requests

st.set_page_config(page_title="SQL → Pandas", layout="wide")
st.title("SQL → Pandas Translator")

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

sql = st.text_area("SQL", height=200, placeholder="SELECT * FROM tabla WHERE col = 1 LIMIT 10;")

if st.button("Traducir"):
    if not sql.strip():
        st.warning("Pega una SQL primero.")
    else:
        try:
            r = requests.post(f"{API_BASE_URL}/translate", json={"sql": sql}, timeout=30)
            r.raise_for_status()
            pandas_code = r.json().get("pandas", "")
            st.session_state["pandas_code"] = pandas_code
        except Exception as e:
            st.error(f"Error llamando al backend: {e}")

st.subheader("Código Pandas")
st.code(st.session_state.get("pandas_code", "# Aquí aparecerá el resultado"), language="python")