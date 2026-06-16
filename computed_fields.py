from pydantic import BaseModel , EmailStr , computed_field
from typing import List, Dict 

#DATA VALIDATION USING PYDANTIC

class Patient(BaseModel):

    name: str
    age: int 
    email: EmailStr        
    weight: float       #kg
    height: float      #mtr     
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height ** 2), 2)
        return bmi

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.bmi)
    print("Updated")

patient_info = {'name': 'Sanjeevani', 'age': 20, 'email': 'sm2020@icici.com', 'weight': 55.5, 'height': 1.7, 'married': False, 'allergies': ['Peanuts'], 'contact_details': {'email': 'sm2020@gmail.com', 'phone': '1234567890'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)