from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import app_payu_wc_transactions
from routes import app_payu_hub_card

from database import mysql
from settings import ENVIRONMENT

app = FastAPI()

@app.get('/')
def read_root():
    return{"welcome":"API is working."}

@app.on_event('startup')
def connect_db():
    mysql.sql_conn = mysql.db_connection()

if ENVIRONMENT == 'prod':
    origins = ['https://payments-1001-angular.web.app']
else:
    origins = ['https://payments-1001-angular.development.web.app', 'http://localhost:4200']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(app_payu_wc_transactions, prefix='/api/payu-latam')

app.include_router(app_payu_hub_card, prefix='/api/payu-hub')
