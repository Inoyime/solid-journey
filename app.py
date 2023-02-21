import streamlit as st

st.title("Título")
opciones=("o1","o2","o3")
respuesta1=st.radio("Pregunta",opciones)

if respuesta1=="o2":
  st.write("estupendo")
if respuesta1=="o1":
  st.write("no, eso no es una opción")
if respuesta1=="o3":
  st.write("ok")
