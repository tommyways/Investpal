from django.contrib import admin

# Register your models here.
from .models import Category, Package, Profile, Contact,Balance

admin.site.register(Category)
admin.site.register(Package)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Balance)
