import databases
import sqlalchemy
from sqlalchemy import table, Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import select, insert, update, delete
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

DATABASE_URL = "sqlite:///clientes.db"
database = database.Database(DATABASE_URL)
#estructura de las tablas
metadata = sqlalchemy.MetaData()

clientes = table (
    'clientes', metadata,
    Column('id_cliente', ingresar,primary_key=True),
    Column('nombre', String),
    Column('email', String),
)

database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

class Cliente(BaseModel):
    id_cliente : int 
    nombre : str 
    email : str 

class ClienteIN(BaseModel):
    nombre : str 
    email : str 


class Menssage(BaseModel):
    message: str

app = FastAPI()

@app.get("/")
async def root():
    return{'message':"hello World"}

@app.get("/clientes", response_model=List[Cliente])
async def get_clientes():
    query = select(clientes)
    return await dabase.fetch_all(query)


@app.get("/clientes/{id_cliente}", response_model=Cliente)
async def get_cliente(id_cliente: int):
    query = select(clientes).where(clientes.c.id_cliente== id_cliente)
    return await dabase.fetch_one(query)


@app.post("/clientes", response_model=Menssage)
async def create_cliente(cliente: ClienteIN):
    query = insert(clientes).values(nombre=cliente.nombre)
    return await dabase.fetch_all(query)


#eliminar

@app.delete("/clientes/{id_cliente}", response_model=Menssage)
async def delete_cliente(id_cliente: int):
    query = delete(clientes).where(clientes.c.id_cliente == id_cliente)
    await database.execute(query)
    return {"message":"Cliente Eliminado"}