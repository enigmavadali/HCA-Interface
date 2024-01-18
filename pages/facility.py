import streamlit as st
from streamlit_option_menu import option_menu

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
    options=["Data Entry", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)