# Generated by Django 4.0.3 on 2022-03-03 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('hospitality', 'hospitality'), ('headquarter', 'headquarter'), ('residential', 'residential'), ('retail', 'retail'), ('scenography', 'scenography')], db_index=True, max_length=100, unique=True, verbose_name="project's category name")),
                ('photo', models.ImageField(default=None, upload_to='category_covers/', verbose_name='cover photo')),
            ],
            options={
                'verbose_name': 'Categories',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MainPageCoverPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='', upload_to='cover_photos/', verbose_name='cover photo')),
                ('order', models.SmallIntegerField(default=1, verbose_name='cover photos order')),
            ],
            options={
                'verbose_name': 'Cover photos',
                'verbose_name_plural': 'Cover photos',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=100, verbose_name='project name')),
                ('caption', models.CharField(blank=True, default='', max_length=100, verbose_name='project caption')),
                ('project_photo', models.ImageField(default=None, upload_to='project_covers/', verbose_name='cover photo')),
                ('order', models.SmallIntegerField(default=1, verbose_name='display order')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Projects',
                'verbose_name_plural': 'Projects',
                'ordering': ['category', 'order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, default='', max_length=255, verbose_name='photo caption')),
                ('photo', models.ImageField(default=None, upload_to='photos/', verbose_name='photo')),
                ('order', models.SmallIntegerField(default=1, verbose_name='display order')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='data creation time')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='data update time')),
                ('is_published', models.BooleanField(default=True, verbose_name='is to publish')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'Pictures of projects',
                'verbose_name_plural': 'Pictures of projects',
                'ordering': ['project', 'order'],
            },
        ),
    ]
