# Generated by Django 4.0.6 on 2022-07-22 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_replycomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='private',
            field=models.BooleanField(default=False, null=True),
        ),
    ]