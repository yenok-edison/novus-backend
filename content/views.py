from django.http import JsonResponse
from .models import Course, Service, TeamMember


def get_content(request):
    courses = []
    for course in Course.objects.all():
        courses.append({
            "id": course.id,
            "title": course.title,
            "description": course.description,
            "price": course.price,
            "category": course.category,
            "image": course.image.url if course.image else "",
            "link": course.link,
            "points": [p.text for p in course.points.all()]
        })

    services = [
        {
            "id": s.id,
            "title": s.title,
            "description": s.description,
            "image": s.image.url if s.image else "",
            "date": s.date,
            "url": s.url
        }
        for s in Service.objects.all()
    ]

    team = [
        {
            "id": t.id,
            "name": t.name,
            "designation": t.designation,
            "description": t.description,
            "image": t.image.url if t.image else "",
        }
        for t in TeamMember.objects.all()
    ]

    return JsonResponse({
        "course": courses,
        "services": services,
        "ourteam": team
    })




def course_detail(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return JsonResponse({"error": "Course not found"}, status=404)

    return JsonResponse({
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "price": course.price,
        "category": course.category,
        "image": course.image.url if course.image else "",
        "points": [p.text for p in course.points.all()]
    })


def course_list(request):
    courses = [
        {
            "id": c.id,
            "title": c.title,
            "description": c.description,
            "category": c.category,
            "image": c.image.url if c.image else "",
        }
        for c in Course.objects.all()
    ]

    return JsonResponse({"courses": courses})


def service_list(request):
    services = Service.objects.all()

    data = []
    for service in services:
        data.append({
            "id": service.id,
            "title": service.title,
            "data": service.date,
            "description": service.description,
            "image": service.image.url if service.image else "",
        })

    return JsonResponse(data, safe=False)


def members_list(request):
    members = TeamMember.objects.all()

    data = []
    for member in members:
        data.append({
            "id": member.id,
            "name": member.name,
            "description": member.description,
            "image": member.image.url if member.image else "",
        })

    return JsonResponse(data, safe=False)