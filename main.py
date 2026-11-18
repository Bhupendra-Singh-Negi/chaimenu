from fastapi import FastAPI, Query, HTTPException
from models import MenuItem, MenuResponse
from data import menu_item
app=FastAPI(
    title="Chai Point API",
    description="Read only menu API for kiosk display and mobile app"
)

@app.get("/")
def root():
    return {"message":"Welcome to chai point"}

@app.get("/menu", response_model=MenuResponse)
def get_menu(category: str| None = Query(None, description="Filter by hot drinks, cold drinks, snake, main course")):
    if(category):
        filter= [item for item in menu_item if item["category"].lower()==category.lower()]
        if not filter:
            raise HTTPException(status_code=404,detail=f"No item is found in the category ${category}")
        return MenuResponse(count=len(filter), items=filter)
    return MenuResponse(count=len(menu_item), item=menu_item)

@app.get("/menu/{item_id}", response_model=MenuItem)
def get_item(item_id:int):
    low = 0
    high = len(menu_item) - 1

    while low <= high:
        mid = (low + high) // 2

        if menu_item[mid]["id"] == item_id:
            return menu_item[mid]

        elif menu_item[mid]["id"] < item_id:
            low = mid + 1

        else:
            high = mid - 1
    raise HTTPException(status_code=404,detail=f"item not found for id: ${item_id}")
