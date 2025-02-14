import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase you productivity")


for todo in todos:
    st.checkbox(todos)

st.text_input(label="Enter a todo: ")