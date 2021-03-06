# Generated by Django 4.0 on 2022-03-23 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeEditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProBlem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_description', models.CharField(blank=True, max_length=255, null=True)),
                ('input_style', models.CharField(blank=True, max_length=255, null=True)),
                ('output_style', models.CharField(blank=True, max_length=255, null=True)),
                ('data_range', models.CharField(blank=True, max_length=255, null=True)),
                ('input_sample', models.CharField(blank=True, max_length=255, null=True)),
                ('output_sample', models.CharField(blank=True, max_length=255, null=True)),
                ('problem_degree', models.CharField(blank=True, max_length=255, null=True)),
                ('time_space_limit', models.CharField(blank=True, max_length=255, null=True)),
                ('input', models.CharField(blank=True, max_length=255, null=True)),
                ('output', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
