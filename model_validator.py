from pydantic import BaseModel , EmailStr , AnyUrl , Field, model_validator
from typing import List, Dict , Optional, Annotated

#DATA VALIDATION USING PYDANTIC

class Patient(BaseModel):

    name: str
    age: int 
    email: EmailStr        
    weight: float            
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years old.')
        return model

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Updated")

patient_info = {'name': 'Sanjeevani', 'age': 20, 'email': 'sm2020@icici.com', 'weight': 55.5, 'married': False, 'allergies': ['Peanuts'], 'contact_details': {'email': 'sm2020@gmail.com', 'phone': '1234567890'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)

