from distutils.file_util import move_file
from fastapi import FastAPI
import uvicorn
from finalmodel import recommendation
from pydantic import BaseModel
import starlette
from typing import List
app = FastAPI()

@app.get('/')
def get_root():
  return {'message': 'What Movie would you like to watch today?'}


@app.get('{movie}')
def display_movie(movie: str):
    x = recommendation(movie)
    return {'recommendations': x }




