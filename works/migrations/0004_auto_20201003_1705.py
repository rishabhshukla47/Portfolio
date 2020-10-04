# Generated by Django 3.1.1 on 2020-10-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_work_imageno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='imageno',
        ),
        migrations.AddField(
            model_name='work',
            name='imagesrc',
            field=models.ImageField(default='1', upload_to='static/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]