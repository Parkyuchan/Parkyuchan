# Generated by Django 4.0.3 on 2022-08-15 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_todo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Todo',
        ),
        migrations.AddField(
            model_name='dong',
            name='hook_text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
