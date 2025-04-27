from fastapi import APIRouter
from pydantic import BaseModel

practice_router = APIRouter()

class Item(BaseModel):
    name: str
    desc: str


@practice_router.post("/{item_name}")
def practice_path_endpoint(item_name: str):
    return {"message": f"This is a practice endpoint for {item_name}"} 

@practice_router.post("")
def practice_query_endpoint(param1: int, param2: str):
    return {"message": f"This is a practice endpoint for {param1} and {param2}"}

@practice_router.post("/json/body")
def practice_body_function(item: Item):
    return item