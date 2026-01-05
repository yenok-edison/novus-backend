from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to="courses/")
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class CoursePoint(models.Model):
    course = models.ForeignKey(
        Course, related_name="points", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="services/")
    date = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="team/")

    def __str__(self):
        return self.name
