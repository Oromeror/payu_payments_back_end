from os import path
from typing import Optional
from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import JSONResponse

from interface.payu_wc_transaction import TransactionInfo
from database.mysql import execute_query
from starlette.status import HTTP_409_CONFLICT, HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
import hashlib


app_payu_wc_transactions = APIRouter()

# Method to create a transaction

@app_payu_wc_transactions.post(
    path='/payu_wc_confirmation',
    status_code=HTTP_200_OK,
    tags=['Transactions'],
    summary="Create transaction in MySQL database"
)

async def create_confirmation(
    merchant_id: Optional[int] = Form(None),
    state_pol: Optional[str] = Form(None),
    risk: Optional[float] = Form(None),
    response_code_pol: Optional[str] = Form(None),
    reference_sale: Optional[str] = Form(None),
    reference_pol: Optional[str] = Form(None),
    sign: Optional[str] = Form(None),
    extra1: Optional[str] = Form(None),
    extra2: Optional[str] = Form(None),
    extra3: Optional[str] = Form(None),
    payment_method: Optional[int] = Form(None),
    payment_method_type: Optional[int] = Form(None),
    installments_number: Optional[int] = Form(None),
    value: Optional[float] = Form(None),
    tax: Optional[float] = Form(None),
    additional_value: Optional[float] = Form(None),
    transaction_date: Optional[str] = Form(None),
    currency: Optional[str] = Form(None),
    email_buyer: Optional[str] = Form(None),
    cus: Optional[str] = Form(None),
    pse_bank: Optional[str] = Form(None),
    test: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    billing_address: Optional[str] = Form(None),
    shipping_address: Optional[str] = Form(None),
    phone: Optional[str] = Form(None),
    office_phone: Optional[str] = Form(None),
    account_number_ach: Optional[str] = Form(None),
    account_type_ach: Optional[str] = Form(None),
    administrative_fee: Optional[float] = Form(None),
    administrative_fee_base: Optional[float] = Form(None),
    administrative_fee_tax: Optional[float] = Form(None),
    airline_code: Optional[str] = Form(None),
    attempts: Optional[int] = Form(None),
    authorization_code: Optional[str] = Form(None),
    travel_agency_authorization_code: Optional[str] = Form(None),
    bank_id: Optional[str] = Form(None),
    billing_city: Optional[str] = Form(None),
    billing_country: Optional[str] = Form(None),
    commision_pol: Optional[float] = Form(None),
    commision_pol_currency: Optional[str] = Form(None),
    customer_number: Optional[int] = Form(None),
    paymentDate: Optional[str] = Form(None),
    error_code_bank: Optional[str] = Form(None),
    error_message_bank: Optional[str] = Form(None),
    exchange_rate: Optional[float] = Form(None),
    ip: Optional[str] = Form(None),
    nickname_buyer: Optional[str] = Form(None),
    nickname_seller: Optional[str] = Form(None),
    payment_method_id: Optional[int] = Form(None),
    payment_request_state: Optional[str] = Form(None),
    pseReference1: Optional[str] = Form(None),
    pseReference2: Optional[str] = Form(None),
    pseReference3: Optional[str] = Form(None),
    response_message_pol: Optional[str] = Form(None),
    shipping_city: Optional[str] = Form(None),
    shipping_country: Optional[str] = Form(None),
    transaction_bank_id: Optional[str] = Form(None),
    transaction_id: Optional[str] = Form(None),
    payment_method_name: Optional[str] = Form(None),
    date: Optional[str] = Form(None),
    franchise: Optional[str] = Form(None),
    bank_referenced_name: Optional[str] = Form(None),
    operation_date: Optional[str] = Form(None),
    cc_holder: Optional[str] = Form(None),
    antifraudMerchantId: Optional[int] = Form(None),
    transaction_type: Optional[str] = Form(None),
    cc_number: Optional[str] = Form(None),
    cardType: Optional[str] = Form(None),
    account_id: Optional[int] = Form(None),
    bank_referenced_code: Optional[str] = Form(None),
    pseCycle: Optional[str] = Form(None)
    ):
    transaction = {
        'merchant_id': merchant_id,
        'state_pol': state_pol,
        'risk': risk,
        'response_code_pol': response_code_pol,
        'reference_sale': reference_sale,
        'reference_pol': reference_pol,
        'sign': sign,
        'extra1': extra1,
        'extra2': extra2,
        'extra3': extra3,
        'payment_method': payment_method,
        'payment_method_type': payment_method_type,
        'installments_number': installments_number,
        'value': validate_zeros(value),
        'tax': tax,
        'additional_value': additional_value,
        'transaction_date': transaction_date,
        'currency': currency,
        'email_buyer': email_buyer,
        'cus': cus,
        'pse_bank': pse_bank,
        'test': test,
        'description': description,
        'billing_address': billing_address,
        'shipping_address': shipping_address,
        'phone': phone,
        'office_phone': office_phone,
        'account_number_ach': account_number_ach,
        'account_type_ach': account_type_ach,
        'administrative_fee': administrative_fee,
        'administrative_fee_base': administrative_fee_base,
        'administrative_fee_tax': administrative_fee_tax,
        'airline_code': airline_code,
        'attempts': attempts,
        'authorization_code': authorization_code,
        'travel_agency_authorization_code': travel_agency_authorization_code,
        'bank_id': bank_id,
        'billing_city': billing_city,
        'billing_country': billing_country,
        'commision_pol': commision_pol,
        'commision_pol_currency': commision_pol_currency,
        'customer_number': customer_number,
        'paymentDate': paymentDate,
        'error_code_bank': error_code_bank,
        'error_message_bank': error_message_bank,
        'exchange_rate': exchange_rate,
        'ip': ip,
        'nickname_buyer': nickname_buyer,
        'nickname_seller': nickname_seller,
        'payment_method_id': payment_method_id,
        'payment_request_state': payment_request_state,
        'pseReference1': pseReference1,
        'pseReference2': pseReference2,
        'pseReference3': pseReference3,
        'response_message_pol': response_message_pol,
        'shipping_city': shipping_city,
        'shipping_country': shipping_country,
        'transaction_bank_id': transaction_bank_id,
        'transaction_id': transaction_id,
        'payment_method_name': payment_method_name,
        'date': date,
        'franchise': franchise,
        'bank_referenced_name': bank_referenced_name,
        'operation_date': operation_date,
        'cc_holder': cc_holder ,
        'antifraudMerchantId': antifraudMerchantId,
        'transaction_type': transaction_type,
        'cc_number': cc_number,
        'cardType': cardType,
        'account_id': account_id,
        'bank_referenced_code': bank_referenced_code,
        'pseCycle': pseCycle
    }

    if validate_signature(transaction['merchant_id'],
            transaction['reference_sale'],
            transaction['value'],
            transaction['currency'],
            transaction['state_pol'],
            transaction['sign']) == True :
        query_path = path.join("transactions", "create_transaction.sql")
        execute_query(query_name=query_path, fetch_data=False, fetch_one=False, **transaction)
        return "success"
    else:
        raise HTTPException(status_code=400, detail="The signature is not valid")


def validate_zeros(value: float):
    new_value: float
    before_dec, after_dec = str(value).split('.')
    if  after_dec == '00':
        new_value = float('.'.join((before_dec, after_dec[0:1])))
    elif after_dec != '00':
        new_value = float('.'.join((before_dec, after_dec[0:2])))
    return new_value
    

def generate_mds5_diganture(sign_base: str):
    return hashlib.md5(sign_base.encode('utf-8')).hexdigest()

def generate_sha1_diganture(sign_base: str):
    return hashlib.sha1(sign_base.encode('utf-8')).hexdigest()

def generate_sha256_diganture(sign_base: str):
    return hashlib.sha256(sign_base.encode('utf-8')).hexdigest()    

def validate_signature(merchant_id: str,
            reference_sale: str,
            value: float,
            currency: str,
            state_pol: str,
            sign: str):

    apiKey = '4Vj8eK4rloUd272L48hsrarnUA'
    sign_base = '%s~%s~%s~%s~%s~%s' % (apiKey,merchant_id,reference_sale,value,currency,state_pol)

    if sign==generate_mds5_diganture(sign_base) or sign==generate_sha1_diganture(sign_base) or sign==generate_sha256_diganture(sign_base): 
        valid_sign = True  
    else:
        valid_sign = False
    return valid_sign
