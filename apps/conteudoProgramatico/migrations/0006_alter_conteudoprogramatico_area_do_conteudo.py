# Generated by Django 4.2.4 on 2023-09-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conteudoProgramatico', '0005_alter_conteudoprogramatico_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conteudoprogramatico',
            name='area_do_conteudo',
            field=models.CharField(max_length=200, verbose_name='Área do Conteúdo'),
        ),
    ]