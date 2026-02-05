from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import auth_controller, task_controller

app = FastAPI(title="Task Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
