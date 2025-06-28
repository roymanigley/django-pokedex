from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Trainer(models.Model):
    user_profile = models.ForeignKey(
        get_user_model(), on_delete=models.DO_NOTHING,
        verbose_name=_('User Profile')
    )

    def __str__(self) -> str:
        print(self.id)
        return str(self.user_profile)

    class Meta:
        verbose_name = _('Trainer')
        verbose_name_plural = _('Trainers')
        ordering = ('user_profile__first_name', 'user_profile__last_name',)


class TrainerPokemon(models.Model):
    trainer = models.ForeignKey(
        'Trainer', on_delete=models.DO_NOTHING,
        verbose_name=_('Trainer')
    )
    pokemon = models.ForeignKey(
        'core.Pokemon', on_delete=models.DO_NOTHING,
        verbose_name=_('Pokémon')
    )
    level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name=_('Level')
    )

    def __str__(self) -> str:
        return f'{self.pokemon} ({self.trainer})'

    class Meta:
        verbose_name = _('Trainer Pokémon')
        verbose_name_plural = _('Trainer Pokémons')
        ordering = (
            'trainer__user_profile__first_name',
            'trainer__user_profile__last_name',
            'pokemon__pokemon_id',
        )
