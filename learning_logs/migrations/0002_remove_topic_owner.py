# Generated by Django 5.0.3 on 2024-04-02 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='owner',
        ),
    ]
