# Generated by Django 4.0 on 2022-03-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_problem_problem_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='problem_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
