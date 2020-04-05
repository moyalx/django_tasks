# Generated by Django 3.0.3 on 2020-04-04 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tasks_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.person'),
        ),
    ]
