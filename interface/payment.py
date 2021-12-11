from typing import Optional
from pydantic import BaseModel

class Payment(BaseModel):
    amount: str
    currency: str
    statement_soft_descriptor: str