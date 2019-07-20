# Generated by Django 2.2.3 on 2019-07-20 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='collections',
            field=models.ManyToManyField(related_name='collections', to='collection.Collection'),
        ),
        migrations.AlterField(
            model_name='article',
            name='specification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specification', to='article.Specification'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='tag.Tag'),
        ),
        migrations.AlterField(
            model_name='article',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='theme', to='theme.Theme'),
        ),
    ]
