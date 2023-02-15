from django.contrib import admin
from .models import *

admin.site.register(Stores)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Client)

