# Generated by Django 4.2.16 on 2024-12-04 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='descripcionUsuario',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
