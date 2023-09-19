from django.contrib import admin
from .models import Person,Collection,Item,Cart
# Register your models here.
admin.site.register(Person)
admin.site.register(Collection)
admin.site.register(Item)
admin.site.register(Cart)