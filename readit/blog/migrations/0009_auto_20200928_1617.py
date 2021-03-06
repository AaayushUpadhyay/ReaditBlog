# Generated by Django 3.0.7 on 2020-09-28 10:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20200925_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='dislikes',
            field=models.ManyToManyField(default=None, related_name='blog_articles_dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(default=None, related_name='blog_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
