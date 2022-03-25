# Generated by Django 4.0.3 on 2022-03-22 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectionTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='file description')),
                ('date', models.DateTimeField(verbose_name='upload date and time')),
                ('video', models.FileField(blank=True, null=True, upload_to='upload_video/', verbose_name='upload video')),
                ('count_objects', models.IntegerField(blank=True, null=True, verbose_name='count find objects')),
                ('count_image', models.IntegerField(blank=True, null=True, verbose_name='count save images')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='run_creator', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
            options={
                'verbose_name': 'Table with data uploaded for detection',
                'verbose_name_plural': 'Table with data uploaded for detection',
            },
        ),
        migrations.CreateModel(
            name='TrackerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('navigationtime', models.DateTimeField()),
                ('imei', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Table with data from GLONASS tracker',
                'verbose_name_plural': 'Table with data from GLONASS tracker',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.FileField(upload_to='', verbose_name='image path')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='location latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='location longitude')),
                ('count_objects', models.IntegerField(blank=True, null=True, verbose_name='count find objects in image')),
                ('date_table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='detection.detectiontable')),
            ],
            options={
                'verbose_name': 'Table save image',
                'verbose_name_plural': 'Table save images',
            },
        ),
    ]
