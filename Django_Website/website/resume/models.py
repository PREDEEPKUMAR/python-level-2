from django.db import models

# Create your models here.


class Details(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=100, default='NULL')
    designation = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name + ' - ' + self.designation


class Skills(models.Model):
    name = models.ForeignKey(Details, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=200)
    percentage = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name + ' - ' + self.percentage


class Language(models.Model):
    name = models.ForeignKey(Details, on_delete=models.CASCADE)
    language_name = models.CharField(max_length=200)
    expertise = models.CharField(max_length=50)

    def __str__(self):
        return self.language_name + ' - ' + self.expertise