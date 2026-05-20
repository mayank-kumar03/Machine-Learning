from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def hello():
      return {'message':'Hello world'}

@app.get("/myself")
def myself():
      return {'intro':'developer'}