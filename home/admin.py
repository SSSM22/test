from django.contrib import admin
from .models import Averages,StudentMaster,StudentScores, Announcement

# Register your models here.
admin.site.register(Averages)
admin.site.register(StudentMaster)
admin.site.register(StudentScores)
admin.site.register(Announcement)