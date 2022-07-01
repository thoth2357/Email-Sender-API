from fastapi import APIRouter, HTTPException
from Schema import SmtpSchema
from Controller import create_transport, build_mail

router = APIRouter(
    prefix="/api/smtp"
)


@router.post("/send")
async def send_mail(request: SmtpSchema):
    """sends email"""
    sender = create_transport("server224.web-hosting.com", request.Port, "mailman@playpadd.app", "ZX~}m2(l$6Q9")
    if not sender:
        raise HTTPException(
            status_code=500,
            detail="could not create transport for smtp server.check Credentials"
        )
    message = build_mail("mailman@playpadd.app", request.To, request.Subject, request.Body)
    try:
        sender.sendmail("mailman@playpadd.app", request.To, message)
        return f"email sent successfully"
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="could not send email"
        )
