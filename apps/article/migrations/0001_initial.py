# Generated by Django 2.2.3 on 2019-08-20 02:59

import apps.article.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collection', '0004_auto_20190819_2031'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('identifier', models.CharField(max_length=255, unique=True)),
                ('author', models.CharField(max_length=100)),
                ('license', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=255, null=True)),
                ('created', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(null=True, upload_to=apps.article.models.Article.file_directory)),
                ('collections', models.ManyToManyField(related_name='collections', to='collection.Collection')),
                ('tags', models.ManyToManyField(related_name='tags', to='tag.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('platform', models.CharField(blank=True, max_length=100, null=True)),
                ('installation', models.CharField(blank=True, max_length=100, null=True)),
                ('extension', models.CharField(blank=True, max_length=100, null=True)),
                ('meta', models.TextField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_specification', to='article.Article')),
            ],
        ),
    ]
