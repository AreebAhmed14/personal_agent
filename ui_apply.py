from main import shajees
import streamlit as st

st.set_page_config(page_title="shajees.assistant" , page_icon ="shajees.png")
st.header("SHAJEES 🌸 ASSISTANT ")

user = st.chat_input("Ask about shajeeah...")

if user:
  st.info(f"{user}")

if user:
    result = shajees(user)
    st.write(result)
