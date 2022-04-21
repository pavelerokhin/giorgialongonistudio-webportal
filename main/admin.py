from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_html_photo', 'photo')
    list_display_links = ('name', 'get_html_photo', 'photo')

    fields = ('name', 'photo', 'get_html_photo_big')
    readonly_fields = ('get_html_photo_big',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50 />')

    def get_html_photo_big(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=350 />')

    get_html_photo.short_description = "Project category's photo"
    get_html_photo_big.short_description = "Project category's photo"


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order', 'get_html_photo', 'project_photo')
    list_display_links = ('name', 'category', 'order', 'project_photo')
    search_fields = ['category__name','name']

    def get_html_photo(self, object):
        if object.project_photo:
            return mark_safe(f'<img src="{object.project_photo.url}" width=50 />')

    def get_html_photo_big(self, object):
        if object.project_photo:
            return mark_safe(f'<img src="{object.project_photo.url}" width=350 />')

    fields = ('name', 'category', 'caption', 'order', 'project_photo', 'get_html_photo_big')
    readonly_fields = ('get_html_photo_big', )

    get_html_photo.short_description = "Photo"
    get_html_photo_big.short_description = "Photo"

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'get_html_photo', 'photo', 'order')
    list_display_links = ('project', )
    list_editable = ('caption',)
    search_fields = ('project__name', )

    fields = ('project', 'caption', 'get_html_photo_big', 'photo', 'order')
    readonly_fields = ('get_html_photo_big', )

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50 />')

    def get_html_photo_big(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=350 />')

    get_html_photo.short_description = "Photo"
    get_html_photo_big.short_description = "Photo"


class MainPageCoverPhotosAdmin(admin.ModelAdmin):
    list_display = ('get_html_photo', 'photo', 'order')
    list_display_links = ('get_html_photo', 'photo')

    fields = ('get_html_photo_big', 'photo', 'order', )
    readonly_fields = ('get_html_photo_big', )

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50 />')

    def get_html_photo_big(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=350 />')

    get_html_photo.short_description = "Main page cover's photo"
    get_html_photo_big.short_description = "Main page cover's photo"


admin.site.register(MainPageCoverPhotos, MainPageCoverPhotosAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Photo, PhotoAdmin)

admin.site.site_title = 'Giorgia Longoni Studio'
admin.site.site_header = 'Giorgia Longoni studio administration'
