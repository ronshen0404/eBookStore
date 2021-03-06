# Generated by Django 4.0.4 on 2022-07-05 01:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0006_alter_userbook_book_alter_userbook_comment_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbook',
            name='comment_rating',
        ),
        migrations.AddField(
            model_name='userbook',
            name='comment',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userbook',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]
