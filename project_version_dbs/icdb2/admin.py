from curses.ascii import US
from django.contrib import admin
from .models import User, Roaster, Bean

# Register your models here.
admin.site.register(User)
admin.site.register(Roaster)
admin.site.register(Bean)
