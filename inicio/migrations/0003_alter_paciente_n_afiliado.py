# Generated by Django 5.0.3 on 2024-03-16 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_paciente_n_afiliado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='n_afiliado',
            field=models.CharField(max_length=20),
        ),
    ]
