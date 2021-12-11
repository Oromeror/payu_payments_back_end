from typing import Optional
from pydantic import BaseModel

class Charge(BaseModel):
    amount: str
    currency: str
    statement_soft_descriptor: str

class BillingAddress(BaseModel):
    country: str
    email: str
    first_name: str
    last_name: str
    line1: str
    state: str
    zip_code: str

class ShippingAddress(BaseModel):
    country: str
    email: str
    first_name: str
    last_name: str
    line1: str
    state: str
    zip_code: str