from django.db import models
from django.utils.translation import gettext_lazy as _


class PokemonType(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    created_at = models.DateTimeField(
        editable=False, auto_now_add=True, verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        editable=False, auto_now=True, verbose_name=_('Updated at')
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Pokémon Type')
        verbose_name_plural = _('Pokémon Type')


class Pokemon(models.Model):
    pokemon_id = models.IntegerField(unique=True, verbose_name=_('Pokémon ID'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    height = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Height')
    )
    weight = models.DecimalField(
        max_digits=10, decimal_places=3, verbose_name=_('Weight')
    )
    image = models.ImageField(
        upload_to='pokemon_image', verbose_name=_('Image')
    )
    types = models.ManyToManyField(PokemonType, verbose_name=_('Types'))
    health = models.IntegerField(verbose_name=_('Health'))
    attack = models.IntegerField(verbose_name=_('Attack'))
    defense = models.IntegerField(verbose_name=_('Defense'))
    special_attack = models.IntegerField(verbose_name=_('Special Attack'))
    special_defense = models.IntegerField(verbose_name=_('Special Defense'))
    speed = models.IntegerField(verbose_name=_('Speed'))
    description = models.TextField(
        null=True, blank=True, verbose_name=_('Description')
    )

    created_at = models.DateTimeField(
        editable=False, auto_now_add=True, verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        editable=False, auto_now=True, verbose_name=_('Updated at')
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Pokémon')
        verbose_name_plural = _('Pokémon')
