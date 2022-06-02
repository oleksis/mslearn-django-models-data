from django.contrib import admin

# Register your models here.
from .models import Dog, Shelter

admin.site.register(Shelter)
admin.site.register(Dog)
