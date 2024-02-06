# Generated by Django 5.0.2 on 2024-02-06 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limite', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('tipo', models.CharField(choices=[('c', 'Crédito'), ('d', 'Débito')], max_length=1)),
                ('descricao', models.CharField(max_length=10)),
                ('realizada_em', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transacao.cliente')),
            ],
        ),
    ]