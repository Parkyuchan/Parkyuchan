# Generated by Django 4.0.3 on 2022-08-30 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_pages', '0010_alter_faculty_options_alter_school_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='major',
            options={'verbose_name_plural': '학과'},
        ),
    ]