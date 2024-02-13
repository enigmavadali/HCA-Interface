import streamlit as st
import requests

page_title = "Text to Query"
layout = "centered"
page_icon = ":rocket:"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

api_url = "http://localhost:8080/"

with st.form("Query Form",clear_on_submit=True):
    facility_id = st.text_input("Facility ID:")
    input_text = st.text_area("Query Text:")
    submitted = st.form_submit_button("Submit")

if submitted:
    try:
        # use input text to create query (integrate model call here)
        query = "select * from public.resident where gender=:gender"
        request_body = {
            "query":query,
            "params":{
                "gender":"Male"
            }}
        # NEED TO TAKE CARE OF SQL INJECTION POSSIBILITY!!!!
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        print(request_body)
        response = requests.post(api_url + "runQuery", json=request_body, headers=headers)
        response_data = response.json()
        if response.status_code == 200:
            if isinstance(response_data, list) and response_data:
                st.table(response_data)
            elif isinstance(response_data, dict):
                st.table([response_data])
            else:
                st.error("No valid data received from the API.")
        else:
            st.error(response_data)
    except Exception as e:
        st.error(f"Error making API request: {e}")
