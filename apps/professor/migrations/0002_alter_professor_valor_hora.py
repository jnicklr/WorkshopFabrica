# Generated by Django 4.2.4 on 2023-09-01 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='valor_hora',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
