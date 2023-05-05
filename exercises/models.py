from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone, timedelta

# Create your models here.
class Classification(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField("exercises.Author")
    classification = models.ForeignKey("exercises.Classification", on_delete=models.CASCADE, related_name="exercises", null=True)
    publisher = models.ForeignKey("exercises.Publisher", on_delete=models.CASCADE, null=True)
    publication_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.title}"
    
    def was_published_recently(self):
        date_today = timezone.now().date()
        return self.publication_date >= date_today - timedelta(day=1)
    
    was_published_recently.admin_order_field = "publication_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"
    
class Publisher(models.Model):
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=60, null=True)
    state_province = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=50, null=True)
    website = models.URLField(max_length = 200, null=True)
    
    def __str__(self):
        return self.name
    
class MyUser(User):
    force_logout_date = models.DateTimeField(null=True, blank=True)

    def force_logout(self):
        self.force_logout_date = datetime.now()
        self.save()
    