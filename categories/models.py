from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ThirdCategory(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    sub_categories = models.ForeignKey('SecondCategory', related_name='sub_categories', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = _('ThirdCategories')

    def __str__(self):
        return '%d: %s' % (self.pk, self.name)


class SecondCategory(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    sub_cats = models.ForeignKey('FirstCategory', related_name='sub_cats', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = _('SecondCategories')

    def __str__(self):
        return '%d: %s' % (self.pk, self.name)


class FirstCategory(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = _('FirstCategories')

    def __str__(self):
        return self.name



