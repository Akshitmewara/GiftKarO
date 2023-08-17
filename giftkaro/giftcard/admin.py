from django.contrib import admin

from giftcard.models import Giftcard

# Register your models here.
class GiftCardsAdmin(admin.ModelAdmin):
    # Specify the fields you want to display in the admin list view
    list_display = ('name', 'img', 'disc')

# Register your models here.
admin.site.register(Giftcard,GiftCardsAdmin)