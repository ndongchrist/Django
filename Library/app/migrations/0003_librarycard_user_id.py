# Generated by Django 4.2.1 on 2023-05-09 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_librarycard_user_id_librarycard_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarycard',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
