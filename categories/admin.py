from django.contrib import admin
from .models import FirstCategory, SecondCategory, ThirdCategory


# Register your models here.
class ThirdCategoryInLine(admin.TabularInline):
    model = ThirdCategory
    #list_display = ('id', 'name', 'date')
    #list_display_links = ('id', 'name')
    #search_fields = ('id', 'name')


class SecondCategoryInLine(admin.TabularInline):
    model = SecondCategory
    #list_display = ('id', 'name', 'date')
    #list_display_links = ('id', 'name')
    #search_fields = ('id', 'name')


    inlines = [ThirdCategoryInLine]


class FirstCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


    inlines = [SecondCategoryInLine]


admin.site.register(FirstCategory, FirstCategoryAdmin)
admin.site.register(SecondCategory)
admin.site.register(ThirdCategory)
