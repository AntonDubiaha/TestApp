from django.db import models

# Create your models here.


class ThirdCategory(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    sub_categories = models.ForeignKey('SecondCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SecondCategory(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    sub_cats = models.ForeignKey('FirstCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FirstCategory(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



