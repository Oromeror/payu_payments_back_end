from typing import Optional
from pydantic import BaseModel

class Card(BaseModel):
    card_number: str
    expiration_date: str
    holder_name: str
    token_type: str
    identity_document_type: str
    identity_document_number: str

    def get_card(BaseModel):
        return BaseModel
