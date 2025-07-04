# Generated by Django 5.2.3 on 2025-06-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=10)),
                ('image', models.ImageField(upload_to='pokemon_image')),
                ('health', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('special_attack', models.IntegerField()),
                ('special_defense', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('types', models.ManyToManyField(to='core.pokemontype')),
            ],
        ),
    ]
