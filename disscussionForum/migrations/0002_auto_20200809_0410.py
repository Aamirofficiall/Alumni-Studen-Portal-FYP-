# Generated by Django 3.0.7 on 2020-08-08 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disscussionForum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dissforum',
            options={'ordering': ['datePosted']},
        ),
    ]
