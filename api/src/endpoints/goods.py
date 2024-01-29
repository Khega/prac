from fastapi import APIRouter, HTTPException
from fastapi.params import Body
from api.src.utils.db import db_get_data, db_update_item, db_delete_item

router = APIRouter()

@router.get("/goods/{item_id}")
async def read_item(item_id: int, q: str = None):
    query = f"SELECT * FROM goods WHERE id = {item_id}"
    result = db_get_data(query)
    return {"item_id": item_id, "q": q, "data": result}

@router.put("/goods/{item_id}")
async def update_item(item_id: int, updated_item: dict = Body(...)):
    query = f"UPDATE goods SET name = '{updated_item['name']}', price = {updated_item['price']} WHERE id = {item_id}"
    result = db_get_data(query)
    return {"message": f"Item with id {item_id} updated successfully"}

@router.post("/goods")
async def create_item(item: dict = Body(...)):
    query = f"INSERT INTO goods (name, price) VALUES ('{item['name']}', {item['price']})"
    result = db_get_data(query)
    return {"message": "Item created successfully"}

@router.patch("/goods/{item_id}")
async def patch_item(item_id: int, updated_item: dict = Body(...)):
    query = f"UPDATE goods SET name = '{updated_item['name']}', price = {updated_item['price']} WHERE id = {item_id}"
    result = db_get_data(query)
    return {"message": f"Item with id {item_id} updated successfully"}

@router.get("/goods")
async def get_all_items():
    query = "SELECT * FROM goods"
    result = db_get_data(query)
    return {"data": result}

@router.delete("/goods/{item_id}")
async def delete_item(item_id: int):
    query = f"DELETE FROM goods WHERE id = {item_id}"
    result = db_get_data(query)
    return {"message": f"Item with id {item_id} deleted successfully"}
