# Generated by Django 4.1.2 on 2022-11-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('try_wiki_app', '0002_content_type_subcontent_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content_type',
            name='keyID',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subcontent_type',
            name='Sub_keyID',
            field=models.CharField(max_length=255),
        ),
    ]
