# Generated by Django 4.0.3 on 2022-03-18 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0002_rename_count_pothole_detectedtable_count_objects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='count_img_pothole',
            new_name='count_objects',
        ),
    ]