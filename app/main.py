from fastapi import FastAPI

app = FastAPI(
    title="Issue Tracker API",
    version="1.0.0")

items = []
@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items[item_id]
    return item