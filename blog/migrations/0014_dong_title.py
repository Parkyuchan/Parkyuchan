# Generated by Django 4.0.3 on 2022-08-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_dong'),
    ]

    operations = [
        migrations.AddField(
            model_name='dong',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]