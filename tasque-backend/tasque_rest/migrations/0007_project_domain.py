# Generated by Django 3.0.5 on 2020-06-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasque_rest', '0006_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='domain',
            field=models.CharField(choices=[('personal', 'Personal'), ('work', 'Work')], default='personal', max_length=10),
        ),
    ]
