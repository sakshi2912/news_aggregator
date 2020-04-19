from django.contrib import admin
from .models import covid1,fullmore,weatherdetails,technews,worldnews
# Register your models here.
admin.site.register(fullmore)
admin.site.register(covid1)
admin.site.register(weatherdetails)
admin.site.register(technews)
admin.site.register(worldnews)
