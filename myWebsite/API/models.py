from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    age=models.PositiveIntegerField(default=15)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=50)
    email=models.EmailField()
    web=models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


