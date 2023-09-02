# Generated by Django 4.2.4 on 2023-09-02 20:59

import apps.aluno.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0003_alter_aluno_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(help_text='O formato deve ser: xxx.xxx.xxx-xxx', max_length=14, validators=[apps.aluno.models.validar_cpf]),
        ),
    ]
