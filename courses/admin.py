from django.contrib import admin

# Register your models here.
from . models import Course,Learning,Prerequisite,Tag, Video,Usercourse,Payment


class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin,LearningAdmin,PrerequisiteAdmin]



admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(Usercourse)
admin.site.register(Payment)
