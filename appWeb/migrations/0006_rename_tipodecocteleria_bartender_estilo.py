# Generated by Django 4.0.4 on 2022-06-09 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appWeb', '0005_rename_tipo_de_cocteleria_bartender_tipodecocteleria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bartender',
            old_name='tipoDeCocteleria',
            new_name='Estilo',
        ),
    ]