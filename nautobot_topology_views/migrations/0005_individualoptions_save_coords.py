# Generated by Django 4.1.8 on 2023-05-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_topology_views', '0004_coordinategroup_coordinate'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualoptions',
            name='save_coords',
            field=models.BooleanField(default=False),
        ),
    ]
