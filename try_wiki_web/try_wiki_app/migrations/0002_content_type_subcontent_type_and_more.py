# Generated by Django 4.1.1 on 2022-11-09 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('try_wiki_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyID', models.IntegerField()),
                ('keyValue', models.TextField()),
                ('Info_Key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='try_wiki_app.information')),
            ],
        ),
        migrations.CreateModel(
            name='SubContent_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_keyID', models.IntegerField()),
                ('Sub_keyValue', models.TextField()),
                ('SubKey_Description', models.TextField()),
                ('level_Info', models.IntegerField()),
                ('Content_Key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='try_wiki_app.content_type')),
            ],
        ),
        migrations.RemoveField(
            model_name='main_info',
            name='Main_key',
        ),
        migrations.DeleteModel(
            name='Info_Meta',
        ),
        migrations.DeleteModel(
            name='Main_Info',
        ),
    ]
