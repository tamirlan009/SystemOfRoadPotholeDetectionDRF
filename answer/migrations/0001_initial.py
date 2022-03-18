# Generated by Django 4.0.3 on 2022-03-15 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0004_rename_leadtime_task_leaddatetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300, verbose_name='answer description')),
                ('replyDate', models.DateTimeField(auto_now=True, verbose_name='date and time create answer')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='task.task', verbose_name='related task')),
            ],
            options={
                'verbose_name': 'Table with answer',
                'verbose_name_plural': 'Table with answers',
                'ordering': ('-replyDate',),
            },
        ),
        migrations.CreateModel(
            name='AnswerImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(blank=True, null=True, upload_to='task_answer/', verbose_name='answer image')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answerImages', to='answer.answer', verbose_name='related answer')),
            ],
            options={
                'verbose_name': 'Table with answer image',
                'verbose_name_plural': 'Table with answer images',
            },
        ),
    ]