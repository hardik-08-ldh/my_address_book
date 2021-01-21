from django.contrib import admin
from address_book import models
# Register your models here.

admin.site.register(
    models.Address,
)