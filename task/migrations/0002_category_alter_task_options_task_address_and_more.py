# Generated by Django 4.0.3 on 2022-03-15 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='category name')),
            ],
            options={
                'verbose_name': 'Table with task category',
                'verbose_name_plural': 'Table with task categories',
            },
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-createDateTime',), 'verbose_name': 'Table with task', 'verbose_name_plural': 'Table with tasks'},
        ),
        migrations.AddField(
            model_name='task',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='location address'),
        ),
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executor', to=settings.AUTH_USER_MODEL, verbose_name='task executor'),
        ),
        migrations.AddField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='Task is done or not'),
        ),
        migrations.AddField(
            model_name='task',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='location latitude'),
        ),
        migrations.AddField(
            model_name='task',
            name='leadTime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='task lead date and time'),
        ),
        migrations.AddField(
            model_name='task',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='location longitude'),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(blank=True, null=True, upload_to='single_task/')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='task.task', verbose_name='related task')),
            ],
            options={
                'verbose_name': 'Table with task image',
                'verbose_name_plural': 'Table with task images',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='task.category', verbose_name='task category'),
        ),
    ]
