# Generated by Django 4.1.4 on 2022-12-21 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_alter_autor_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='IdPrestamo',
        ),
        migrations.AlterField(
            model_name='prestamos',
            name='IdUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.usuario'),
        ),
    ]
