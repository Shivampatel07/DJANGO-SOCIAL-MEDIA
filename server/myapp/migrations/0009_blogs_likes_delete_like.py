# Generated by Django 4.1.7 on 2023-10-05 08:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='likes',
            field=models.ManyToManyField(default=1, related_name='user_Likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
