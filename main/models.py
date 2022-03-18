from django.db import models

CATEGORIES = (
    ('hospitality', 'hospitality'),
    ('headquarter', 'headquarter'),
    ('residential', 'residential'),
    ('retail', 'retail'),
    ('scenography', 'scenography'),
)


class Category(models.Model):
    name = models.CharField(max_length=100,
                            db_index=True,
                            verbose_name='project\'s category name',
                            choices=CATEGORIES,
                            unique=True
                            )
    photo = models.ImageField(upload_to="category_covers/", default=None,
                              verbose_name='cover photo')

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True,
                                 verbose_name='category')
    name = models.CharField(max_length=100, default='', db_index=True, verbose_name='project '
                                                                                    'name')
    caption = models.CharField(max_length=100, default='', blank=True, verbose_name='project caption')
    project_photo = models.ImageField(upload_to="project_covers/", default=None,
                              verbose_name='cover photo')
    order = models.SmallIntegerField(default=1,
                                     verbose_name='display order')

    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "Projects"
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return self.name


class Photo(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True,
                                verbose_name='project')
    caption = models.CharField(max_length=255, default='', blank=True,
                               verbose_name='photo caption')
    photo = models.ImageField(upload_to="photos/", default=None,
                              verbose_name='photo')
    order = models.SmallIntegerField(default=1,
                                     verbose_name='display order')
    time_create = models.DateTimeField(auto_now_add=True, blank=True,
                                       verbose_name='data creation time')
    time_update = models.DateTimeField(auto_now=True, blank=True,
                                       verbose_name='data update time')
    is_published = models.BooleanField(default=True,
                                       verbose_name='is to publish')

    class Meta:
        verbose_name = "Pictures of projects"
        verbose_name_plural = "Pictures of projects"
        ordering = ['project', 'order']


class MainPageCoverPhotos(models.Model):
    photo = models.ImageField(upload_to="cover_photos/", default='', verbose_name='cover photo')
    order = models.SmallIntegerField(default=1, verbose_name='cover photos order')

    class Meta:
        verbose_name = "Cover photos"
        verbose_name_plural = "Cover photos"
        ordering = ['order']
