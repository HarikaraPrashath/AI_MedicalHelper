from fastapi import APIRouter, UploadFile, File
from typing import List
from modules.load_vectorstore import load_vectorstore
from fastapi.responses import JSONResponse
from logger import logger

router = APIRouter()

@router.post("/upload_pdf/")
async def upload_pdfs(file:List[UploadFile]=File(...)):
    try:
        logger.info("Received PDF upload files")
        load_vectorstore(file)
        logger.info("Documents added to vector store successfully")
        return {"message":"File processed and added to vector store successfully"}
    except Exception as e:
        logger.exception("Error uploading PDFs: %s", e)
        return JSONResponse(status_code=500, content={"message": "Internal server error"})