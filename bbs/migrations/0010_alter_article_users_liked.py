# Generated by Django 4.0.3 on 2022-04-14 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0009_alter_article_users_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='users_liked',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
    ]
