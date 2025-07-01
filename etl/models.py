from pydantic import BaseModel, EmailStr

# Modelo de dirección

class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str

# Modelo de Ususrio

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: Address