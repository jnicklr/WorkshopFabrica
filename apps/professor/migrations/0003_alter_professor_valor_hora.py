# Generated by Django 4.2.4 on 2023-09-02 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_alter_professor_valor_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='valor_hora',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor da Hora'),
        ),
    ]
