# Generated by Django 5.1.4 on 2024-12-28 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_privatemessage_guest_sender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatechatroom',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
