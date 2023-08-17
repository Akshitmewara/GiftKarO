from django.contrib import admin
from cart.models import Cards

class CardsAdmin(admin.ModelAdmin):
    # Specify the fields you want to display in the admin list view
    list_display = ('giftcard_id','name', 'img', 'disc', 'code')

# Register your models here.
admin.site.register(Cards,CardsAdmin)
