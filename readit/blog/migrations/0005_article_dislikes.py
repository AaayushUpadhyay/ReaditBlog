# Generated by Django 3.0.7 on 2020-09-24 13:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_article_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='dislikes',
            field=models.ManyToManyField(related_name='blog_articles_dislike', to=settings.AUTH_USER_MODEL),
        ),
    ]
