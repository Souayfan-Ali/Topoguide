# Generated by Django 4.0.4 on 2022-04-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraires', '0002_sortie_commentaire_alter_itineraire_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraire',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='commentaire',
            field=models.TextField(default=''),
        ),
    ]