# Generated by Django 3.1.2 on 2020-10-24 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_auto_20201023_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='posted_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
