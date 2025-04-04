# Generated by Django 4.2.7 on 2025-03-31 18:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='ano_lancamento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='filme',
            name='estudio',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='filme',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema.genero'),
        ),
        migrations.AlterField(
            model_name='filme',
            name='nome_do_filme',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='genero',
            name='nome_genero',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sobrenome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
    ]
