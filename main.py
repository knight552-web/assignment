from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder



app=FastAPI()

a=[]
class Name(BaseModel):
    studentname:str
    studentid:str
    age:int

@app.get("/")
def basic():
    return "Welcome"

@app.get("/student")
def det(name:Name):
    return a



@app.post("/information")
def name(name:Name):
    a=dict()
    nameenc=jsonable_encoder(name)
    f=nameenc['studentname']
    i= nameenc['studentid']
    age=nameenc['age']
    item.update({"student name":f,
    "student id":i,
    "student_age":age})
    a.append(item)
    return "registered"

@app.put("/information/{studentid}")
async def update_item(studentid:str,name:Name):
    update_item=jsonable_encoder(name)
    for p in a:
        if p['student id']==studentid:
             p['student_age']=23
    return a

@app.put("information/age/{studentage}")
def del_item(student_age: str,name:Name):
    for p in a:
        if p['student_age'] == student_age:
            a.remove(p)
    return a
