# Generated by Django 3.1.7 on 2021-04-06 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=128)),
                ('contend', models.FileField(upload_to='contend')),
                ('image', models.FileField(upload_to='image')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=128)),
                ('contend', models.FileField(upload_to='contend')),
                ('image', models.FileField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='vet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=128)),
                ('contend', models.FileField(upload_to='contend')),
                ('image', models.FileField(upload_to='image')),
            ],
        ),
    ]