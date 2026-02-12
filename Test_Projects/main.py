import requests
import streamlit as st

st.header("CRUD Application")
base_url = "http://127.0.0.1:8000"
res = requests.get(base_url +"/read")
data = res.json()

@st.dialog("ADD NAME")
def add_name():
    name = st.text_input("NAME",placeholder="Enter the name")
    is_c = st.button("DONE",type="primary",use_container_width=True)
    if is_c:
        data = {"name": name}
        requests.post(base_url +"/create/list",json=data)
        st.rerun()

cols = st.columns([1,2,1])
with cols[0] :
    st.subheader('TASKIFY')
with cols[2] :
    is_clicked = st.button('Add task',type="primary",use_container_width=True)
    if is_clicked :
        add_name()
st.divider()

for t in data :
    with st.container(border=True):
        st.subheader(t["name"])
        st.button("edit", key=f"update_{t['id']}")
        st.button("delete", key=f"delete_{t['id']}")