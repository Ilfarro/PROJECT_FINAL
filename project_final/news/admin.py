from django.contrib import admin
from .models import News
# Register your models here.

my_model = [News]
admin.site.register(my_model)