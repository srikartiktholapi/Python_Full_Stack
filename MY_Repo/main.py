from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse
from supabase import create_client

db_url = "https://exjkkbjgzxftynuixyag.supabase.co"
db_key = "sb_publishable_KzhC-Wbjwd52h8ns_vub8g_JP2r46pZ"

db= create_client(db_url,db_key)


app = FastAPI()
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Backend deployed successfully on Vercel 🚀"
    }

# Getting all the task 
@app.get("/tasks")
def get_tasks():
      result = db.table("Tasks").select("*").execute()
      tasks = result.data
      return tasks


#adding the tasks 
@app.post("/add/task")
async def add_task(request : Request):
    data = await request.json()
    results = db.table("Tasks").insert(data).execute()
    return {"Successfully sent"}
#Getting a specific task depending on the id 
@app.get("/task/")
def get_task(task_id :int):
    result =db.table("Tasks").select("*").eq("id",task_id).execute()
    return result.data

#Updating a specific tasks 
@app.put("/task/{task_id}")
async def add_task(request : Request ,task_id :int):
    data = await request.json()
    results = db.table("Tasks").update(data).eq('id',task_id).execute()
    return {"message":"Updated Successfully"}


#Deleting the a specific tasks 
@app.delete("/task/{task_id}")
def deletion_task(task_id : int):
    results = db.table("Tasks").delete().eq("id",task_id).execute()
    return {"message": "deleted successfully"}