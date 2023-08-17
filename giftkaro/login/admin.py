from django.contrib import admin
from login.models import UserData

admin.site.site_header = "Devendra Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Admin Portal"

# Register your models here.
admin.site.register(UserData)