# Generated by Django 3.2.18 on 2023-05-02 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_recomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_comment',
        ),
        migrations.AlterModelTable(
            name='comment',
            table=None,
        ),
    ]