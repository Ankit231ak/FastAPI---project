# 👩‍⚕️ Patient Management System

A simple CRUD (Create, Read, Update, Delete) API for managing patient records, built with **FastAPI** and a **Streamlit** frontend. Patient data is persisted in a local JSON file (`p.json`).

The system automatically calculates the **Body Mass Index (BMI)** and provides a **verdict** (Underweight, Normal, Overweight, Obese) for each patient based on their height and weight.

## 🎬 Demo

<video src="Patient Management.mp4" controls></video>

---

## ✨ Features

### Backend (FastAPI - `main.py`)

* **View Patients:**
    * `GET /`: Basic welcome message.
    * `GET /about`: API information.
    * `GET /view`: Retrieve all patient records.
    * `GET /patient/{patient_id}`: Retrieve a specific patient by ID.
    * `GET /sort`: Sort all patients by `height`, `weight`, or `bmi` in ascending (`asc`) or descending (`desc`) order.
* **CRUD Operations:**
    * `POST /create`: Add a new patient. The request body uses the `Patient` Pydantic model.
    * `PUT /edit/{patient_id}`: Update an existing patient's details. The request body uses the `PatientUpdate` Pydantic model, allowing for partial updates.
    * `DELETE /delete/{patient_id}`: Remove a patient record.
* **Data Models (`Patient` and `PatientUpdate`):** Pydantic models with validation for fields like `age` (must be $>0$ and $<120$), `height` and `weight` (must be $>0$).
* **Computed Fields:** The `Patient` model includes computed fields for automatically calculating **`bmi`** and **`verdict`**.

### Frontend (Streamlit - `app.py`)

A user-friendly web interface with tabs for all functionalities:

* **View Patients:** Displays all patient data in a table, with a 'Reload Patients' button.
* **Add Patient:** A form to create a new patient record.
* **Update Patient:** A form to update an existing patient's details by ID. Supports updating only specific fields.
* **Delete Patient:** Input to delete a patient by ID.
* **Sort Patients:** Interface to select fields (`height`, `weight`, `bmi`) and order (`asc`, `desc`) for sorting.
* **Find Patient:** Input to search and display one or more patients by comma-separated IDs.

---

## 🛠️ Setup and Installation

### Prerequisites

You need **Python 3.8+** installed on your system.

### 1. Clone the repository (or set up files)

Ensure you have the following files in your project directory:
* `main.py` (FastAPI backend)
* `app.py` (Streamlit frontend)
* `p.json` (Patient data storage)
* `Patient Management.mp4` (Demo video)

### 2. Install Dependencies

Create a virtual environment (optional, but recommended) and install the necessary Python packages:

```bash
# Optional: Create and activate a virtual environment
# python -m venv venv
# source venv/bin/activate  # On Linux/macOS
# .\venv\Scripts\activate   # On Windows

