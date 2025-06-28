import l4py
import json
from apps.trainer.models import Trainer, TrainerPokemon
from apps.core.models import Pokemon
from apps.authentication.models import UserProfile
import requests
from django.core.files.base import ContentFile

logger = l4py.get_logger('Data Initializer')

TrainerPokemon.objects.all().delete()
Trainer.objects.all().delete()


trainers = [
    {
        'first_name': 'Ash',
        'last_name': 'Ketchum',
        'image': 'https://www.pokewiki.de/images/thumb/f/f0/Ash_SWSH_Artwork.png/195px-Ash_SWSH_Artwork.png',
        'pokemons': [
            {'pokemon_id': 25, 'level': 80}
        ]
    },
    {
        'first_name': 'Rocko',
        'last_name': 'from Marmoria City',
        'image': 'https://www.pokewiki.de/images/thumb/1/12/Rocko_LGPE_Artwork.png/255px-Rocko_LGPE_Artwork.png',
        'pokemons': [
            {'pokemon_id': 95, 'level': 70}
        ]
    },
    {
        'first_name': 'Misty',
        'last_name': 'from Azuria City',
        'image': 'https://www.pokewiki.de/images/thumb/5/5b/Misty_LGPE_Artwork.png/300px-Misty_LGPE_Artwork.png',
        'pokemons': [
            {'pokemon_id': 121, 'level': 60}
        ]
    },
]

for trainer in trainers:
    user_profile = UserProfile.objects.get_or_create(
        username=trainer['first_name'],
        defaults={
            'first_name': trainer['first_name'],
            'last_name': trainer['last_name'],
            'is_superuser': False,
            'is_staff': False,
            'is_active': True,
        }
    )[0]

    image_content = requests.get(trainer['image']).content
    user_profile.image.save(
        trainer['first_name'], ContentFile(image_content), save=True,
    )
    user_profile.set_password(trainer['first_name'])
    user_profile.save()

    trainer_model = Trainer.objects.create(
        user_profile=user_profile
    )

    for pokemon in trainer['pokemons']:
        TrainerPokemon.objects.create(
            pokemon=Pokemon.objects.get(pokemon_id=pokemon['pokemon_id']),
            trainer=trainer_model,
            level=pokemon['level'],
        )
