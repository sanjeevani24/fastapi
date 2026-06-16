from fastapi import FastAPI, Path ,HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A Fully Functional Patient Management System API built with FastAPI."}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = 'ID of the Patient in the DB', example = 'P001')):
# load all the data first.  the three dots in path means that the parameter is required used to add description and example to the parameter in the docs.
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found.")
    
@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description = 'Field to sort the patients by'),
order: str = Query('asc', description = 'Sort in ascending (asc) or descending (desc) order')):
    
    Valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in Valid_fields:
        raise HTTPException (status_code=400, detail=f'Invalid field Select From: {Valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException (status_code=400, detail = 'Invalid order. Choose "asc" or "desc".')
    
    data = load_data()

    sort_order =True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse= sort_order)

    return sorted_data

