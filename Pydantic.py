from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List, Dict , Optional, Annotated

#TYPE VALIDATION USING PYDANTIC field function is used to add additional validation rules to the field.  gt means greater than, lt means less than, strict means that the value must be of the specified type and cannot be coerced to that type.  default means that the field is not required and can be None.  description is used to add a description to the field in the docs.
class Patient(BaseModel):

    name: Annotated[str, Field(max_length = 50, title='Name of the Patient')]  #CAN ADDDESCRIPTION, TITLE, EXAMPLE, MAX_LENGTH, MIN_LENGTH, REGEX ETC.  TO THE FIELD USING FIELD FUNCTION.  ANNOTATED IS USED TO ADD ADDITIONAL METADATA TO THE FIELD.
    age: int = Field(gt=0, lt=120)
    email: EmailStr         #Data validation for email using pydantic
    website: Optional[AnyUrl] = None        #Data validation for URL using pydantic.  Optional means that the field is not required and can be None.
    weight: Annotated[float, Field(gt=0, strict=True)]             #Data validation for weight using pydantic.  gt means greater than 0.  Field is used to add additional validation rules to the field.
    married: Annotated[bool, Field(default=None, description='Marital status of the patient')]  #Data validation for boolean using pydantic.  default means that the field is not required and can be None.
    allergies: Annotated[Optional[List[str]], Field(max_length = 5, default=None)]
    contact_details: Dict[str, str]
    
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age) 
    print("Inserted")

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.website)
    print(patient.email)
    print("Updated")

patient_info = {'name': 'Sanjeevani', 'age': 20, 'email': 'sm2020@gmail.com', 'weight': 55.5, 'married': False, 'contact_details': {'email': 'sm2020@gmail.com', 'phone': '1234567890'}}

patient1 = Patient(**patient_info)

#insert_patient_data(patient1)
update_patient_data(patient1)

#DATA VALIDATION USING PYDANTIC



