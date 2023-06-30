from django.contrib import admin

from .models import Event, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Event)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = (
        "title",
        "type",
    )
    list_editable = ("type",)
    search_fields = ("type",)
    list_filter = ("type",)
    # empty_value_display = "-пусто-"


admin.site.register(Image)
