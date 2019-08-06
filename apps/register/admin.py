from django.contrib import admin
from . import models

class VGC_Admin(admin.ModelAdmin):
	pass

admin.site.register(models.VGC, VGC_Admin)