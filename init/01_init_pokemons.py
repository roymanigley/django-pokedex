import l4py
import json
from apps.core.models import Pokemon, PokemonType
import requests
from django.core.files.base import ContentFile

logger = l4py.get_logger('Data Initializer')

Pokemon.objects.all().delete()
PokemonType.objects.all().delete()

types_map = {}
with open('./init/data_types.json') as f:
    types = json.load(f)
    for t in types:
        logger.info('creating PokemonType %s', t)
        types_map[t] = PokemonType.objects.create(name=t)

with open('./init/data_pokemon.json') as f:
    pokemons = json.load(f)
    for p in pokemons:
        logger.info('creating Pokemon %s', p['name'])
        types = p.pop('types', [])
        pokemon = Pokemon.objects.create(
            **p,
        )
        pokemon.types.set([types_map[t] for t in types])
        content = requests.get(p['image']).content
        pokemon.image.save(
            f'{pokemon.name}.png'.lower(), ContentFile(content=content), save=True
        )

logger.info(
    'Completed: %s PokemonTypes, %s Pokemons',
    PokemonType.objects.count(),
    Pokemon.objects.count(),
)
