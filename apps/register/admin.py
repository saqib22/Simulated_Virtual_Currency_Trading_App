from django.contrib import admin
from . import models

class VGC_Admin(admin.ModelAdmin):
	def has_add_permission(self, request):
		count = models.VGC.objects.all().count()
		if count == 0:
			return True
		return False

admin.site.register(models.VGC, VGC_Admin)