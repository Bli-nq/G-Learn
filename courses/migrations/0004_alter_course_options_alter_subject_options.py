# Generated by Django 4.1 on 2022-10-16 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_content_options_alter_module_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['title']},
        ),
    ]
