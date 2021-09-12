from django.contrib import admin
from .models import Password, Confirm, Referral

admin.site.register(Password)
admin.site.register(Confirm)
admin.site.register(Referral)