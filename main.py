from typing import List

from fastapi import FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models import Client
from schemes import ClientCreate, ClientResponse
from database import db_conn
from create_db import create_tables
from http_errors import NotFoundError



app = FastAPI()




@app.exception_handler(HTTPException)
async def handle_http_errors(request: Request, exc: HTTPException):
    code = getattr(exc, 'code')
    field = getattr(exc, 'field', None)
    msg = getattr(exc, 'detail')
    
    
    error_msg = {
        'code': code,
        'field': field,
        'msg': msg
    }
    
    return JSONResponse(status_code=exc.status_code, content=error_msg)



@app.get('/test')
def test():
    print('OK')
    return 'OK'


@app.post('/create-interested')
async def create_interested(db: db_conn, client_name: str=Body(...)) -> dict[str, str]:
   client = Client(name=client_name)
   
   db.add(client)
   db.commit()
   db.refresh(client)
   
   return {'client_id': client.id} # type: ignore






@app.get('/clients')
def get_clients(db: db_conn) -> List[ClientResponse]:
   return db.query(Client).all() # type: ignore
   
   
   

@app.post('/update/{client_id}', status_code=200)
def update_client(db: db_conn, client_id: str, client_data: ClientCreate):
   client = db.query(Client).filter(Client.id == client_id).first()
   
   [setattr(client, attr, v) for attr, v in client_data.model_dump(exclude_unset=True).items()]
   
   db.commit()
   
   
   return 'Ok'


@app.post('/score/{client_id}')
def earn_score(db: db_conn, client_id: str, score: int=Body(...)) -> ClientResponse:
   
   client = db.query(Client).filter(Client.id == client_id).first()
   print(score)
   if not client:
      raise NotFoundError(status_code=404, code='not_found', field='client_id', detail='Client not found')
   
   client.score += score # type: ignore
   db.commit()
   db.refresh(client)
   
   return client
   
   
   
   

