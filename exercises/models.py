from django.db import models

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
    author = models.ForeignKey("exercises.Author", on_delete=models.CASCADE, related_name="exercises")
    classification = models.ForeignKey("exercises.Classification", on_delete=models.CASCADE, related_name="exercises", null=True)
    publisher = models.ForeignKey("exercises.Publisher", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"
    
class Publisher(models.Model):
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=60, null=True)
    state_province = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=50, null=True)
    website = models.URLField(max_length = 200, null=True)
    
    def __str__(self):
        return self.name
    
    
    