import streamlit as st
from streamlit_option_menu import option_menu
import requests
from datetime import date

# General data settings 

# resident_fields = ["pid", "firstName", "lastName", "room", "gender", "age", "dob", 
#                    "telephone", "hasPet", "weightLbs", "photo", "emergencyContact1", 
#                    "telephoneEmc1", "relationshipEmc1", "emergencyContact2", "telephoneEmc2", 
#                    "relationshipEmc2", "isAmbulatory", "isAbleToCommunicate", "medicalInformation", 
#                    "isVaccinatedForCovid19", "lastFall", "lastErVisit", 
#                    "dischargedFromOvernightHospitalStay", "isFallRisk", "isWanderRisk", 
#                    "isElopementRisk", "physician", "physicianTelephone", "isPet"]

resident_fields = {
    "pid": int,
    "firstName": str,
    "lastName": str,
    "room": int,
    "gender": str,
    "age": int,
    "dob": date,
    "telephone": str,
    "hasPet": str,
    "weightLbs": int,
    "photo": str,
    "emergencyContact1": str,
    "telephoneEmc1": str,
    "relationshipEmc1": str,
    "emergencyContact2": str,
    "telephoneEmc2": str,
    "relationshipEmc2": str,
    "isAmbulatory": str,
    "isAbleToCommunicate": str,
    "medicalInformation": str,
    "isVaccinatedForCovid19": str,
    "lastFall": date,
    "lastErVisit": date,
    "dischargedFromOvernightHospitalStay": str,
    "isFallRisk": str,
    "isWanderRisk": str,
    "isElopementRisk": str,
    "physician": str,
    "physicianTelephone": str,
    "isPet": str
}

page_title = "Facility Data Entry"
layout = "centered"
page_icon = ":hospital:"

st.set_page_config(page_title=page_title, page_icon=page_icon,layout=layout)
st.title(page_title + " " + page_icon)

selected = option_menu(
    menu_title=None,
    options=["Add Resident", "Data Visualization"],
    # icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)

if selected == "Add Resident":
    with st.form("Resident form", clear_on_submit=True):
        for field, data_type in resident_fields.items():
            if data_type == str:
                st.text_input(f"{field}:", key=field)
            elif data_type == int:
                st.number_input(f"{field}:", key=field)
            elif data_type == date:
                st.date_input(f"{field}:", key=field)
        submitted = st.form_submit_button("save resident")
        if submitted:
            request = {field: st.session_state[field] for field in resident_fields.keys()}
            print(request)
            
            # Send the data as a JSON POST request to the API
            api_url = "your_api_endpoint_here"
            headers = {"Content-Type": "application/json"}
            response = requests.post(api_url, json=request, headers=headers)
            
            if response.status_code == 200:
                st.success("Data saved successfully!")
            else:
                st.error(f"Failed to save data. Status code: {response.status_code}")
