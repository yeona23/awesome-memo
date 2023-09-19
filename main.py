from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


class Memo(BaseModel):
    id: int
    content: str


memos = []

app = FastAPI()


@app.get("/memos")
def read_memo():
    return memos


@app.post("/memos")
def create_memo(memo: Memo):
    memos.append(memo)
    return "success!!!!!!"


@app.put("/memos/{memo_id}")
def put_memo(req_memo: Memo):
    for memo in memos:
        if memo.id == req_memo.id:
            memo.content = req_memo.content
            return "success"
    return "none"


@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):
    for index, memo in enumerate(memos):
        if memo.id == memo.id:
            memos.pop(index)
            return "success"
    return "none"


# print(memos)


app.mount("/", StaticFiles(directory="static", html=True), name="static")
