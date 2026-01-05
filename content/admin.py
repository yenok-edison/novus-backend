from django.contrib import admin
from .models import Course, CoursePoint, Service, TeamMember


class CoursePointInline(admin.TabularInline):
    model = CoursePoint
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price")
    inlines = [CoursePointInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "designation")
