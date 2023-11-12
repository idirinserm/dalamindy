from django.contrib import admin
from .models import Programme, Course, Video, Text

class VideoInline(admin.StackedInline):
    model = Video
    extra = 1

class TextInline(admin.StackedInline):
    model = Text
    extra = 1

class CourseInline(admin.StackedInline):
    model = Course
    extra = 1
    inlines = [VideoInline, TextInline]

class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title', 'description',)
    inlines = [CourseInline]

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'programme',)
    search_fields = ('title', 'programme__title',)
    list_filter = ('programme',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'course',)
    search_fields = ('title', 'course__title',)
    list_filter = ('course__title',)

class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'course',)
    search_fields = ('title', 'course__title',)
    list_filter = ('course__title',)

admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Text, TextAdmin)
