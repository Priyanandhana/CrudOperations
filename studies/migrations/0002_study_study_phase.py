# Generated by Django's makemigrations
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_name', models.CharField(max_length=100)),
                ('study_description', models.TextField()),
                ('sponsor_name', models.CharField(max_length=100)),
                ('study_phase',
                 models.ForeignKey(to='studies.Phase', on_delete=models.CASCADE, db_column='study_phase')),
            ],
        ),
    ]

