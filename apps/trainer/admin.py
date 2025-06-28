from django.contrib import admin
from django.contrib.admin import ModelAdmin
from apps.trainer import models
from django.utils.html import mark_safe
from django.conf import settings
from django.utils.translation import gettext_lazy as _


@admin.register(models.TrainerPokemon)
class TrainerPokemonAdminModel(ModelAdmin):
    list_display = (
        'id', 'get_name', 'get_types', 'get_image_pokemon', 'get_image_trainer'
    )
    list_filter = (
        'trainer', 'pokemon', 'pokemon__types',
    )
    autocomplete_fields = ('trainer', 'pokemon')

    def get_queryset(self, request):
        return models.TrainerPokemon.objects.select_related(
            'trainer__user_profile'
        )

    def get_name(self, instance: models.TrainerPokemon) -> str:
        return instance.pokemon.name

    def get_types(self, instance: models.TrainerPokemon) -> list[str]:
        return [t.name for t in instance.pokemon.types.all()]

    def get_image_pokemon(self, instance: models.TrainerPokemon) -> str:
        return mark_safe(f'<img src="{settings.MEDIA_URL}{instance.pokemon.image}" height="150" />')

    def get_image_trainer(self, instance: models.TrainerPokemon) -> str:
        return mark_safe(f'<img src="{settings.MEDIA_URL}{instance.trainer.user_profile.image}" height="150" />')

    get_name.short_description = _('Name')
    get_types.short_description = _('Types')
    get_image_pokemon.short_description = _('Pokémon')
    get_image_trainer.short_description = _('Trainer')


@admin.register(models.Trainer)
class TrainerAdminModel(ModelAdmin):
    list_display = ('id', 'get_first_name', 'get_last_name', 'get_image')
    search_fields = ('user_profile__first_name', 'user_profile__last_name')

    def get_image(self, instance: models.Trainer) -> str:
        return mark_safe(f'<img src="{settings.MEDIA_URL}{instance.user_profile.image}" height="150" />')

    def get_first_name(self, instance: models.Trainer) -> str:
        return instance.user_profile.first_name

    def get_last_name(self, instance: models.Trainer) -> str:
        return instance.user_profile.last_name

    get_image.short_description = _('Image')
    get_first_name.short_description = _('Firstname')
    get_last_name.short_description = _('Lastname')
