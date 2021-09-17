# Generated by Django 3.2.7 on 2021-09-17 16:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='enroll', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
