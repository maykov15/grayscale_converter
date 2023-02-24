import streamlit as st
import functions

todos = functions.get_todos()

st.title("-= My Todo App =-")
st.subheader("A simple productivity app")
st.write("Add tasks and check them off as you complete them")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")