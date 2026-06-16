from pydantic import BaseModel 

class Address(BaseModel):

    street: str
    city: str
    state: str
    pin_code: str

class patient(BaseModel):

    name: str
    age: int
    address: Address

address_dict = {'street': '123 Main St', 'city': 'Mumbai', 'state': 'Maharashtra', 'pin_code': '400012'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Sanjeevani', 'age': 20, 'address': address1}

patient1 = patient(**patient_dict) 

temp = patient1.model_dump(include = ['name', 'age'])        # converts the pydantic model to a dictionary

print(temp)
print(type(temp))

temp1 = patient1.model_dump_json(exclude= {'address':['state']})      # converts the pydantic model to a json string

print(temp1)
print(type(temp1))

#exclude_unset = True --- IGNORE the field which has not been defined---
