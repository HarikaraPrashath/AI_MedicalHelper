from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware
from routes.upload_pdf import router as upload_router
from routes.ask_questions import router as ask_router

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
app.include_router(upload_router)

#2.asking query
app.include_router(ask_router)
