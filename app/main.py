from fastapi import FastAPI
from cache_manager import CACHE_OBJECT
from gpt_manager import ask_ai
import uvicorn
app = FastAPI()


def check_existing_question(func):
    def wrapper(question: str):
        print(question)
        with CACHE_OBJECT as cache:
            value = cache.connection.get(question)
        if value:
            return {"question": question, "answere": bytes(value).decode()}
        return func(question)

    return wrapper


@app.post("/ask/")
@check_existing_question
def SSA(question: str):
    result = ask_ai(question)
    if not result:
        return {"message":"AI is busy, try later."}
    with CACHE_OBJECT as cache:
        cache.connection.set(question, result)
    return {"question": question, "answare": result}

if __name__=="__main__":
    uvicorn.run(app,port=800)