from django.contrib import admin
from .models import Person, Yt, Viewed

admin.site.register(Person)
admin.site.register(Yt)
admin.site.register(Viewed)