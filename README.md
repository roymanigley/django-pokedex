# POKéDEX
> A POKéDEX application using Django
## Initial Steps

1. create virtual environment:  
`python -m venv .venv`
2. activate virtual environment:  
`.venv\Scripts\activate # Windows`  
`source .venv/bin/activate # UNIX`
3. install the dependencies:  
`pip install -r requirements.txt`
4. initialize database:  
`python management.py migrate`
5. load the Pokédex data:  
`python management.py shell < init\01_init_pokemons.py # Windows`
`python management.py shell < ./init/01_init_pokemons.py # UNIX`
5. load the Trainer data:  
`python management.py shell < init\02_init_trainers.py # Windows`
`python management.py shell < init/02_init_trainers.py # UNIX`
6. create a superuser for the admin portal:  
`python management.py createsuperuser`

## Run the Django Application
`python management.py runserver`

## Login to the django admin portal:
[http://localhost:8000/admin](http://localhost:8000/admin)
