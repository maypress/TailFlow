from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/test")
async def read_item(id: int = Query(None)):
    if id is None or id == 0:
        return {"status": 200, "message": "Not found"}
    return {"status": 200, "id": id}


@app.get("/")
def read_root():
    return {"message": "Hello world"}