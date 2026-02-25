import streamlit as st
import requests

st.set_page_config(page_title="SQL → Pandas Translator")

st.title("🧠 SQL → Pandas Translator")

sql_query = st.text_area(
    "Introduce tu consulta SQL:",
    height=200,
    placeholder="SELECT col FROM df WHERE col = 5"
)

if st.button("Traducir"):
    if sql_query.strip():
        response = requests.post(
            "http://localhost:8000/translate",
            json={"query": sql_query}
        )

        if response.status_code == 200:
            st.subheader("Código Pandas generado:")
            st.code(response.json()["pandas_code"], language="python")
        else:
            st.error("Error en la traducción")