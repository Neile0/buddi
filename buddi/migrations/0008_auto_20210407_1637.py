# Generated by Django 3.1.7 on 2021-04-07 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buddi', '0007_auto_20210407_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='is_subregion_of',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_region', to='buddi.region'),
        ),
    ]
