# contact/views.py
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Enquiry
# from django.core.mail import send_mail
# from django.conf import settings

# @csrf_exempt
# def submit_enquiry(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         subject = request.POST.get("subject")
#         message = request.POST.get("message")

#         Enquiry.objects.create(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message
#         )

#         send_mail(
#             subject,
#             f"New Enquiry \n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}",
#             settings.DEFAULT_FROM_EMAIL,
#             ["yenok@iktaraa.com"],
#             fail_silently=False,
#         )

#         return JsonResponse({"status": "success"})

#     return JsonResponse({"status": "error"}, status=400)

# contact/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Enquiry
from django.core.mail import send_mail
from django.conf import settings
from threading import Thread


def send_enquiry_email(subject, message, from_email, recipient_list):
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )


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

        email_message = (
            f"New Enquiry\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Subject: {subject}\n"
            f"Message: {message}"
        )
        print("email_message : ", email_message)
        # 🚀 Send email in background
        Thread(
            target=send_enquiry_email,
            args=(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                ["yenok@iktaraa.com"],
            ),
        ).start()

        # ⚡ Respond immediately
        return JsonResponse({"status": "success"}, status=200)

    return JsonResponse({"status": "error"}, status=400)

