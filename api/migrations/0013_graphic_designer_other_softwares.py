# Generated by Django 4.1.1 on 2022-10-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_member_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphic_designer',
            name='other_softwares',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]