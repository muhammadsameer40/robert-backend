from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail

@api_view(["POST"])
def send_contact_email(request):

    name = request.data.get("name")
    email = request.data.get("email")
    subject = request.data.get("subject")
    message = request.data.get("message")

    full_message = f"""
    Name: {name}

    Email: {email}

    Subject: {subject}

    Message:
    {message}
    """

    send_mail(
        subject=f"Contact Form: {subject}",
        message=full_message,
        from_email="sameerimran4004@gmail.com",
        recipient_list=["sameerimran4004@gmail.com"],
    )

    return Response({
        "success": True
    })