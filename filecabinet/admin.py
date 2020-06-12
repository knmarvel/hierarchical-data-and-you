from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
# Register your models here.

from filecabinet.models import File

admin.site.register(File, DraggableMPTTAdmin)
