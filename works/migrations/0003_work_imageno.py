# Generated by Django 3.1.1 on 2020-10-03 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_remove_work_imgsrc'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='imageno',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]