# contact/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Enquiry
from django.core.mail import send_mail
from django.conf import settings

@csrf_exempt
def submit_enquiry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Enquiry.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        send_mail(
            subject,
            f"New Enquiry \n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}",
            settings.DEFAULT_FROM_EMAIL,
            ["soniya@iktaraa.com"],
            fail_silently=False,
        )

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"}, status=400)
