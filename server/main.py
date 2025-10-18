from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware
app=FastAPI(title="Medical Assistance API",description="API for AI Medical chatbot ")

#CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credential=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


#middleware exceptions handlers
app.middleware("http")(catch_exception_middleware)


#routers

#1.upload paf documents
#2.asking query