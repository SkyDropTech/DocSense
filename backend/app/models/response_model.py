from pydantic import BaseModel

class SummaryResponse(BaseModel):
    filename: str
    file_type: str
    word_count: int
    char_count: int
    summary: str