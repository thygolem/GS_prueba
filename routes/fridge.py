from fastapi import APIRouter
from config.dbConfig import conn
from models.fridge import fridges
from schemas.fridge import Fridge

fridge = APIRouter()

@fridge.get('/fridges')
def get_fridges():
    return conn.execute(fridges.select()).fetchall()

@fridge.post('/fridges')
def create_fridges(fridge: Fridge):
    new_fridge_metric = {"id": fridge.id, 
                        "timestamp": fridge.timestamp,
                        "chillerStatus": fridge.chillerStatus, 
                        "temperature": fridge.temperature, 
                        "humidity": fridge.humidity, 
                        "power": fridge.power}
    result = conn.execute(fridges.insert().values(new_fridge_metric))
    print(result)
    return "yes"

