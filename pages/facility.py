import streamlit as st
from streamlit_option_menu import option_menu
import requests

# General data settings 

resident_fields = ["pid", "firstName", "lastName", "room", "gender", "age", "dob", 
                   "telephone", "hasPet", "weightLbs", "photo", "emergencyContact1", 
                   "telephoneEmc1", "relationshipEmc1", "emergencyContact2", "telephoneEmc2", 
                   "relationshipEmc2", "isAmbulatory", "isAbleToCommunicate", "medicalInformation", 
                   "isVaccinatedForCovid19", "lastFall", "lastErVisit", 
                   "dischargedFromOvernightHospitalStay", "isFallRisk", "isWanderRisk", 
                   "isElopementRisk", "physician", "physicianTelephone", "isPet"]

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
        for field in resident_fields:
            st.text_input(f"{field}:", key=field)
        submitted = st.form_submit_button("save resident")
        if submitted:
            fields = {field: st.session_state[field] for field in resident_fields}
            print(fields)
            st.success("Data saved!")