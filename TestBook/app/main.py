from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"the big item": item_id}

from fastapi import FastAPI

from app.routers import users, books

app = FastAPI(title="Personal Library API")

app.include_router(users.router)
app.include_router(books.router)
