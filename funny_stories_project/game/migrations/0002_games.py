# Generated by Django 5.0.6 on 2024-05-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_story', models.CharField(default='', max_length=150)),
                ('list_players', models.TextField(default='')),
                ('story', models.TextField(default='')),
                ('number_of_round', models.TextField(default='')),
                ('data_game', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
