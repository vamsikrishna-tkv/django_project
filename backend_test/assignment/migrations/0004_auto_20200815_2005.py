# Generated by Django 3.1 on 2020-08-15 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0003_auto_20200815_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='assignment.users'),
        ),
    ]
