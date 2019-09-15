from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    experience = models.IntegerField(default=0)
    resume = models.FileField(upload_to='employee/resume/')
    image = models.ImageField(upload_to='employee/images/', null=True)

    def __str__(self):
        return self.name

