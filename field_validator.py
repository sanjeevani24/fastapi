from pydantic import BaseModel , EmailStr , AnyUrl , Field, field_validator
from typing import List, Dict , Optional, Annotated

class Patient(BaseModel):

    name: str
    age: int 
    email: EmailStr        
    weight: float            
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid email domain.')
         
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    @field_validator('age', mode='before')
    @classmethod
    def age_validator(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age must be between 0 and 100.')


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

