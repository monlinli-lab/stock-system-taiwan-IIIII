from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="台股兵法智謀全媒體觀測系統",
    layout="wide"
)

st.title("台股兵法智謀全媒體觀測系統")

html_file = Path("index.html")

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")
    components.html(html_content, height=1800, scrolling=True)
else:
    st.error("找不到 index.html，請確認 index.html 與 app.py 在同一層目錄。")
