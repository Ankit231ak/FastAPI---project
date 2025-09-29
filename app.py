import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000" 

st.set_page_config(page_title="Patient Management", layout="wide")
st.title("Patient Management System")

tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(
    ["View Patients", "Add Patient", "Update Patient", "Delete Patient", "Sort Patients","Find Patient"]
)


# View Patients 
with tab1:
    col1, blank ,col2 = st.columns([1, 4, 1])
    with col1:
      st.header("All Patients")
    
    with col2:
      if st.button("Reload Patients"): 
        st.rerun()
              
    

    res = requests.get(f"{API_URL}/view")
    if res.status_code == 200:
        data = res.json()
        if data:
            patients = []
            for pid, p in data.items():
                patients.append({"id": pid, **p})
            st.dataframe(patients, use_container_width=True)
        else:
            st.info("No patients found.")




# Add Patient 
with tab2:
  st.header("Add New Patient")
  with st.form("add_form"):
      id = st.text_input("Patient ID", "P001").upper()
      name = st.text_input("Name")
      city = st.text_input("City")
      age = st.number_input("Age", min_value=1, max_value=120, step=1)
      gender = st.selectbox("Gender", ["", "male", "female", "others"]) 
      height = st.number_input("Height (m)", min_value=0.1, step=0.01, format="%.2f")
      weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1, format="%.1f")
      submitted = st.form_submit_button("Add Patient")

  if submitted:
      # Validation check
      if not id.strip() or not name.strip() or not city.strip() or not gender:
          st.error("❌ All fields are required. Please fill in every input.")
      else:
          payload = {
              "id": id,
              "name": name,
              "city": city,
              "age": age,
              "gender": gender,
              "height": height,
              "weight": weight,
          }
          res = requests.post(f"{API_URL}/create", json=payload)
          if res.status_code == 200:
              st.success("✅ Patient created successfully")
              st.rerun() 
          else:
              st.error(res.json().get("detail", "Error adding patient"))



# Update Patient
with tab3:
    st.header("Update Patient")
    pid = st.text_input("Enter Patient ID to Update").upper()

    if pid:
        name = st.text_input("New Name (optional)")
        city = st.text_input("New City (optional)")
        age = st.number_input("New Age", min_value=0, max_value=120, value=0)
        gender = st.selectbox("New Gender", ["", "male", "female", "others"])
        height = st.number_input("New Height (m)", min_value=0.0, step=0.01)
        weight = st.number_input("New Weight (kg)", min_value=0.0, step=0.1)

        if st.button("Update"):
            payload = {}
            if name: payload["name"] = name
            if city: payload["city"] = city
            if age > 0: payload["age"] = age
            if gender: payload["gender"] = gender
            if height > 0: payload["height"] = height
            if weight > 0: payload["weight"] = weight

            res = requests.put(f"{API_URL}/edit/{pid}", json=payload)
            if res.status_code == 200:
                st.success("✅ Patient updated successfully")
                st.rerun()

            else:
                st.error(res.json().get("detail", "Error updating patient"))


#\ Delete Patient 
with tab4:
    st.header("Delete Patient")
    pid = st.text_input("Enter Patient ID to Delete").upper()
    if st.button("Delete"):
        res = requests.delete(f"{API_URL}/delete/{pid}")
        if res.status_code == 200:
            st.success("🗑️ Patient deleted")
            st.rerun()

        else:
            st.error(res.json().get("detail", "Error deleting patient"))


# Sort Patient
with tab5:
    st.header("Sort Patients")
    sort_by = st.multiselect("Sort By", ["height", "weight", "bmi"], default=["bmi"])
    order = st.radio("Order", ["asc", "desc"], horizontal=True)

    if st.button("Sort"):
        res = requests.get(f"{API_URL}/sort", params={"sort_by": sort_by, "order": order})
        if res.status_code == 200:
            sorted_data = res.json()
            st.dataframe(sorted_data, use_container_width=True)
        else:
            st.error(res.json().get("detail", "Error sorting patients"))

  
#Find Patient
with tab6:
    st.header("Find Patients")
    ids_input = st.text_input("Enter Patient IDs").upper()

    if st.button("Find"):
        patients = []
        ids = [pid.strip() for pid in ids_input.split(",") if pid.strip()] 

        for pid in ids:
            res = requests.get(f"{API_URL}/patient/{pid}")
            if res.status_code == 200:
                data = res.json()
                if data:
                    patients.append({"id": pid, **data})
            else:
                st.warning(f"Patient {pid} not found")

        if patients:
            st.dataframe(patients, use_container_width=True)
        else:
            st.info("No patients found.")
