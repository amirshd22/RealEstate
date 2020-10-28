# Generated by Django 3.0.7 on 2020-10-25 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CreateHome', '0004_auto_20201025_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellhomes',
            name='user',
        ),
        migrations.AddField(
            model_name='sellhomes',
            name='agent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
