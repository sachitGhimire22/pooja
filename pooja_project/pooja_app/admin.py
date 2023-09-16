from django.contrib import admin
from .models import Person,Collection,Item
# Register your models here.
admin.site.register(Person)
admin.site.register(Collection)
admin.site.register(Item)