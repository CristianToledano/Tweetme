# Generated by Django 2.0.4 on 2018-05-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_remove_tweet_miriam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
