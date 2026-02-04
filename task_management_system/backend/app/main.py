from fastapi import FastAPI
from app.controllers import auth_controller, task_controller

app = FastAPI(title="Task Management System")

app.include_router(auth_controller.router, prefix="/auth", tags=["Auth"])
app.include_router(task_controller.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Task Management System API running"}




# from fastapi import FastAPI

# app = FastAPI(title="Task Management System")

# @app.get("/")
# def root():
#     return {"message": "Task Management System API running"}
