from django.contrib import admin
from . models import addImage

class wallpaper(admin.ModelAdmin):
    list_display=('image','title','des')
    search_fields=('title',)
    list_editable=('title','des')

admin.site.register(addImage,wallpaper)


