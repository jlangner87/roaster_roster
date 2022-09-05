from django.contrib import admin
from .models import Bean, Roaster, User, Retailer

admin.site.register(User)
admin.site.register(Roaster)
admin.site.register(Bean)
admin.site.register(Retailer)
