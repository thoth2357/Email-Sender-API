from pydantic import BaseModel


class SmtpSchema(BaseModel):
    """Schema And Typing for Smtp endpoint"""
    Host: str
    Port: int
    Username: str
    Password: str
    To: str
    From: str
    Subject: str
    Body: str
