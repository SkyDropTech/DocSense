import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_parser import parse_document
from app.services.text_cleaner import clean_text
from app.services.llm_service import generate_summary
from app.models.response_model import SummaryResponse
from app.config import settings

router = APIRouter()

@router.post("/upload", response_model=SummaryResponse)
async def upload_document(file: UploadFile = File(...)):
    allowed_extensions = [".pdf", ".docx", ".txt"]
    ext = os.path.splitext(file.filename)[1].lower()
    
    if ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF, DOCX, and TXT are supported.")
        
    file_path = os.path.join(settings.UPLOAD_DIR, file.filename)
    
    # 1. Save File
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        # 2. Extract Text
        raw_text = parse_document(file_path, file.filename)
        
        # 3. Clean Text
        cleaned_text = clean_text(raw_text)
        
        if not cleaned_text:
            raise HTTPException(status_code=400, detail="Document appears to be empty or unreadable.")
            
        word_count = len(cleaned_text.split())
        char_count = len(cleaned_text)
        
        # 4. Generate Summary
        summary = generate_summary(cleaned_text)
        
        return SummaryResponse(
            filename=file.filename,
            file_type=ext.upper().replace(".", ""),
            word_count=word_count,
            char_count=char_count,
            summary=summary
        )
        
    finally:
        # Cleanup: Remove the file from the server after processing
        if os.path.exists(file_path):
            os.remove(file_path)