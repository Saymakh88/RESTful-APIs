from django.db import models

# Create your models here.
# creating comapny model

class Company(models.Model):
    company_id=models.AutoField(primary_key = True)
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                 ('Non IT','Non IT'),
                                                 ('Mobile phones','Mobile Phones')
                                                 ))
    added_date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField(blank=True)
    position=models.CharField(max_length=200, choices=(('Manager','manager'),
                                                       ('Software Developer','Software Developer'),
                                                       ('Data Analyst','Data Analyst') 
    ))

    company=models.ForeignKey(Company, on_delete=models.CASCADE)


