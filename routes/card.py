from os import path
from fastapi import APIRouter, HTTPException, Request, Header
from interface.card import Card
from database.mysql import execute_query
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
import json
import requests

app_payu_hub_card = APIRouter()

@app_payu_hub_card.post(
    path='/tokens',
    status_code=HTTP_200_OK,
    tags=['Token'],
    summary="Create a card token with PayU Hub API"
)

def create_token(
        request: Card,
        content_type: Optional[str] = Header(None),
        api_version: Optional[str] = Header(None),
        app_id: Optional[str] = Header(None),
        public_key: Optional[str] = Header(None),
        x_payments_os_env: Optional[str] = Header(None)
    ):

    url = "https://api.paymentsos.com/tokens"
    params = {
        "card_number": request.get_card().card_number,
        "expiration_date": request.get_card().expiration_date,
        "holder_name": request.get_card().holder_name,
        "token_type": request.get_card().token_type,
        "identity_document": {
            "type": request.get_card().identity_document_type,
            "number": request.get_card().identity_document_number
        }
    }
    headers = {
        "Content-Type": content_type,
        "api-version": api_version,
        "app-id": app_id,
        "public-key": public_key,
        "x-payments-os-env": x_payments_os_env
    }
    post_response = requests.post(url, json = params, headers = headers)
    print(post_response.content.decode('utf-8'))
    if post_response.status_code == 201:
        return json.loads(post_response.content.decode('utf-8'))






