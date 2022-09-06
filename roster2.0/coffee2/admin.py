from django.contrib import admin
from .models import User, Roaster, Bean, Retailer
# Register your models here.

admin.site.register(User)
admin.site.register(Roaster)
admin.site.register(Bean)
admin.site.register(Retailer)
