# https://huggingface.co/albert-base-v2
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

unmasker = pipeline('fill-mask', model='albert-base-v2')


# print(unmasker("I am a [MASK].")[0]['sequence'])

class Item(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
def root():
    return {"message": "All right, there is a connection."}


@app.post("/predict/")
def predict(item: Item):
    """Предварительно подготовленная модель на английском языке.
    Вместо [MASK] моделирует(подбирает) слово.
    Источник - https://huggingface.co/albert-base-
    Примеры фраз:  I study economics at University., I like apples and  pears., My friend often travels.,
    I always get up at 8 o’clock in the morning., We have a flat in London., He plays football every Saturday.,
    She sometimes listens to the radio"""
    return unmasker(item.text)[0]['sequence']
