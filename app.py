import streamlit as st

st.title("¿Tienes poca imaginación para un título?")
opciones=("¿No?","Sí","Meh")
respuesta1=st.radio("Pregunta",opciones)

if respuesta1=="¿No?":
  st.write("Dame tu imaginación")
if respuesta1=="Sí":
  st.write("Ok...Ya somos dos...")
  st.balloons()
if respuesta1=="Meh":
  st.write("Vale, ni pa' ti ni pa' mí")
