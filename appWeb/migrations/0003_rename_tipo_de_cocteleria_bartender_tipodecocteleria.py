# Generated by Django 4.0.4 on 2022-06-08 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appWeb', '0002_rename_tipococeteleria_bartender_tipo_de_cocteleria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bartender',
            old_name='tipo_De_Cocteleria',
            new_name='tipoDeCocteleria',
        ),
    ]