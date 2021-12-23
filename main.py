from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelWithLMHead
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("t5-small")

model = AutoModelWithLMHead.from_pretrained("t5-small")

translator = pipeline("translation_en_to_de", "t5-small")


class Item(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return translator(item.text)
