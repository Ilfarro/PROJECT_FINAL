from django.contrib import admin
from .models import Contact_us
# Register your models here.

my_model = [Contact_us]
admin.site.register(my_model)