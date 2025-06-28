from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from apps.core import models
from django.utils.html import mark_safe
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class PokemonTypeResource(resources.ModelResource):

    class Meta:
        model = models.PokemonType


class PokemonResource(resources.ModelResource):

    class Meta:
        model = models.Pokemon


@admin.register(models.PokemonType)
class PokemonTypeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 20
    search_fields = ('name',)
    list_editable = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [(
        'General', {
            'fields': ('name',)
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at')
        }
    )]


@admin.register(models.Pokemon)
class PokemonAdmin(ImportExportModelAdmin):
    list_display = ('pokemon_id', 'name', 'get_types', 'get_image',)
    list_per_page = 20
    search_fields = ('pokemon_id', 'name')
    list_filter = ('types',)
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('types',)
    autocomplete_fields = ('types',)
    fieldsets = [(
        'General', {
            'fields': ('name', 'types')
        }),
        ('Detail', {
            'fields': ('description', 'image')
        }),
        ('Statistics', {
            'fields': (
                'height', 'weight', 'health', 'speed', 'attack', 'defense', 'special_attack', 'special_defense'
            )
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at')
        }
    )]
    ordering = ('pokemon_id',)

    def get_image(self, instance: models.Pokemon) -> str:
        return mark_safe(f'<img src="{settings.MEDIA_URL}{instance.image}" height="150" />')

    def get_types(self, instance: models.Pokemon) -> list[str]:
        return [t.name for t in instance.types.all()]

    get_image.short_description = _('Image')
    get_types.short_description = _('Types')
