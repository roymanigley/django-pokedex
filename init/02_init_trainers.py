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
            {'pokemon_id': 18, 'level': 74},   # Pidgeot
            {'pokemon_id': 25, 'level': 80},   # Pikachu
            {'pokemon_id': 6, 'level': 78},    # Charizard
            {'pokemon_id': 143, 'level': 75},  # Snorlax
            {'pokemon_id': 149, 'level': 82},  # Dragonite
        ]
    },
    {
        'first_name': 'Rocko',
        'last_name': 'from Marmoria City',
        'image': 'https://www.pokewiki.de/images/thumb/1/12/Rocko_LGPE_Artwork.png/255px-Rocko_LGPE_Artwork.png',
        'pokemons': [
            {'pokemon_id': 95, 'level': 70},   # Onix
            {'pokemon_id': 76, 'level': 68},   # Golem
            {'pokemon_id': 74, 'level': 57},   # Geodude
        ]
    },
    {
        'first_name': 'Misty',
        'last_name': 'from Azuria City',
        'image': 'https://www.pokewiki.de/images/thumb/5/5b/Misty_LGPE_Artwork.png/300px-Misty_LGPE_Artwork.png',
        'pokemons': [
            {'pokemon_id': 121, 'level': 60},  # Starmie
            {'pokemon_id': 118, 'level': 58},  # Goldeen
            {'pokemon_id': 134, 'level': 56},  # Vaporeon
            {'pokemon_id': 130, 'level': 59},  # Gyarados
        ]
    },
    {
        'first_name': 'Jessie & James',
        'last_name': 'Team Rocket',
        'image': 'https://static.wikia.nocookie.net/the-new-action-squad/images/b/b6/Tweam.png/revision/latest/scale-to-width-down/275?cb=20210105023959',
        'pokemons': [
            {'pokemon_id': 24, 'level': 58},   # Arbok
            {'pokemon_id': 110, 'level': 58},  # Weezing
            {'pokemon_id': 52, 'level': 60},  # Weezing
        ]
    },
    {
        'first_name': 'Gary',
        'last_name': 'Oak',
        'image': 'https://www.pokewiki.de/images/thumb/2/25/Gary_Reisen_Anime.png/285px-Gary_Reisen_Anime.png',
        'pokemons': [
            {'pokemon_id': 3, 'level': 82},    # Venusaur
            {'pokemon_id': 9, 'level': 80},    # Blastoise
            {'pokemon_id': 59, 'level': 78},   # Arcanine
            {'pokemon_id': 65, 'level': 76},   # Alakazam
        ]
    },
    {
        'first_name': 'Giovanni',
        'last_name': 'Team Rocket Boss',
        'image': 'https://www.pokewiki.de/images/4/4c/Giovanni_LGPE_Artwork.png',
        'pokemons': [
            {'pokemon_id': 31, 'level': 80},   # Nidoqueen
            {'pokemon_id': 34, 'level': 80},   # Nidoking
            {'pokemon_id': 112, 'level': 78},  # Rhydon
            {'pokemon_id': 53, 'level': 76},   # Persian
            {'pokemon_id': 105, 'level': 75},  # Marowak
        ]
    },
]

for trainer in trainers:
    logger.info('Creating Trainer: %s %s',
                trainer['first_name'], trainer['last_name'])
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
        logger.info(
            'Relating Pokémon to Trainer: %s %s <-> %s',
            trainer['first_name'], trainer['last_name'], pokemon['pokemon_id']
        )
        TrainerPokemon.objects.create(
            pokemon=Pokemon.objects.get(pokemon_id=pokemon['pokemon_id']),
            trainer=trainer_model,
            level=pokemon['level'],
        )
