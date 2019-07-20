# Generated by Django 2.2.3 on 2019-07-20 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='categories',
            field=models.ManyToManyField(related_name='categories_collection', to='category.Category'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='tags',
            field=models.ManyToManyField(related_name='tags_collection', to='tag.Tag'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='theme_collection', to='theme.Theme'),
        ),
    ]
