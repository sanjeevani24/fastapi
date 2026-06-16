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

print(patient1)
print(patient1.address)
print(patient1.address.city)
print(patient1.address.pin_code)
print(patient1.address.street)
print(patient1.address.state)


