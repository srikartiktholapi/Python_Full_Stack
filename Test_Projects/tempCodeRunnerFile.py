from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse
from supabase import create_client
#Creating a CRUD operation backend part 
app =FastAPI()
db_url = "https://ypbcukppkbedxuenoytb.supabase.co"
db_key = "sb_publishable_hK11T77p5-oNDhbmMnnoUw_hw8sJe9P"
db =create_client(db_url,db_key)
#Home page
@app.get("/")
def root():
    html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>CRUD Home</title>
        </head>
        <body>

            <h1>CRUD Application</h1>

            <ul>
                <li><h3>Create  ----->/create/list </h3></li>
                <li><h3>Read    ----->/read</h3></li>
                <li><h3>Update  ----->/update/{upd_id}</h3></li>
                <li><h3>Delete  ----->/delete/{del_id}</h3></li>
            </ul>

        </body>
        </html>
        """
    return HTMLResponse(html)

# CREATE
@app.post("/create/list")
async def create_list(request :Request):
    data = await request.json()
    result =db.table("List_table").insert(data).execute()
    return {"message":"successfully added the list_name"}

# READ
@app.get("/read")
def read():
    result = db.table("List_table").select("*").execute()
    tasks =result.data
    return tasks

# UPDATE
@app.put("/update/{upd_id}")
async def update(request :Request,upd_id: int):
    data = await request.json()
    results = db.table("List_table").update(data).eq("id",upd_id).execute()
    return {"message": "Updation successfully"}

#DELETE 
@app.delete("/delete/{del_id}")
async def delete(request : Request ,del_id :int):
    results = db.table("List_table").delete().eq("id",del_id).execute()
    return {"message": "deletion successfully"}

