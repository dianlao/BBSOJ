# Generated by Django 4.0.3 on 2022-05-06 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0013_alter_article_users_thmub'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='users_thmub',
            new_name='users_thumb',
        ),
    ]
