# Generated by Django 4.0.3 on 2022-03-22 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('detection', '0001_initial'),
        ('task', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskNotificationTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('new task', 'new_task'), ('answer', 'answer')], max_length=50, verbose_name='notification type')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group', verbose_name='related group')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task', verbose_name='related task')),
            ],
            options={
                'verbose_name': 'Table with notification',
                'verbose_name_plural': 'Table with notifications',
            },
        ),
        migrations.CreateModel(
            name='DetectionNotificationTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('detection finished', 'detection_finished')], max_length=50, verbose_name='notification type')),
                ('detection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detection.detectiontable', verbose_name='related detection table')),
            ],
            options={
                'verbose_name': 'Table with detection notification',
                'verbose_name_plural': 'Table with detection notifications',
            },
        ),
    ]
