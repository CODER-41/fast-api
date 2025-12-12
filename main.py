from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')

def index(limit=10, published: bool =True, sort: Optional[str] = None):

    if published:
     
     return  {'data': f'{limit} blog from the db'}
    
    else:
       return  {'data': f'{limit} blog from the db'}

@app.get('/blog/unpublished')

def unpublished():

    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')

def show(id):
    #fetch blog with id = id
     
    return {'data': id}


@app.get('/blog/{id}/comments')

def comments(id):

    return {'data': {'1' , '2'}}

#Using POST method

class Blog(BaseModel):
   
   title: str

   body:str
   published: Optional[bool]

   #pass



@app.post('/blog')

def create_blog(request: Blog):

    return {'data': f"Blog is created wit title {request.title}"}