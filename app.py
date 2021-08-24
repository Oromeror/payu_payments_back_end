from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import app_transactions
from database import mysql
from settings import ENVIRONMENT

app = FastAPI()

# if ENVIRONMENT == 'prod':
#     origins = ['https://payments-1001-angular.web.app/']
# else:
#     origins = ['http://localhost:4200']

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(app_transactions, prefix='/api')


@app.on_event('startup')
def connect_db():
    mysql.sql_conn = mysql.db_connection()
