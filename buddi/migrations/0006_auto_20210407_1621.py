# Generated by Django 3.1.7 on 2021-04-07 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buddi', '0005_auto_20210407_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animalimages',
            options={'verbose_name': 'Animal Images'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='sitteroperatesinregion',
            options={'verbose_name': "Sitter's Regions"},
        ),
    ]