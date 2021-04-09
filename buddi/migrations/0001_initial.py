# Generated by Django 3.1.7 on 2021-04-09 02:07

import buddi.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('bio', models.CharField(max_length=300)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('is_neutered', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('N/A', 'Prefer not to say')], max_length=3)),
                ('requires_exercise', models.BooleanField()),
                ('exercise_requirement', buddi.models.IntegerRangeField()),
                ('is_displayed', models.BooleanField(default=True)),
                ('image_dir', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('type', models.CharField(max_length=128, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False, unique=True)),
                ('is_parent_region', models.BooleanField(default=True)),
                ('is_subregion_of', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_region', to='buddi.region')),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly_rate', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=300)),
                ('profile_image', models.ImageField(blank=True, default='profile_images/profile_image_placeholder.jpg', upload_to='profile_images')),
                ('profile_url', models.URLField(blank=True, unique=True)),
                ('contact_no', models.CharField(max_length=11)),
                ('is_sitter', models.BooleanField(default=False)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddi.region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SitterOperatesInRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddi.region')),
                ('sitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddi.sitter')),
            ],
            options={
                'verbose_name': "Sitter's Regions",
            },
        ),
        migrations.AddField(
            model_name='sitter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddi.userprofile'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', buddi.models.IntegerRangeField()),
                ('sitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddi.sitter')),
            ],
            options={
                'verbose_name': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='AnimalImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=buddi.models.AnimalImages.image_directory_path)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddi.animal')),
            ],
            options={
                'verbose_name': 'Animal Images',
            },
        ),
        migrations.AddField(
            model_name='animal',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddi.animaltype'),
        ),
        migrations.AddField(
            model_name='animal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddi.userprofile'),
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddi.animal')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddi.animaltype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddi.userprofile')),
            ],
        ),
    ]
