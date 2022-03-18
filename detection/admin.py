from django.contrib import admin
from .models import DetectedTable, Images, TrackerData

admin.site.register([DetectedTable, Images, TrackerData])
