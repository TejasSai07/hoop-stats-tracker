# Generated by Django 5.1.2 on 2024-10-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_player_team_alter_player_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerstats',
            name='is_starter',
            field=models.BooleanField(default=False),
        ),
    ]