# Generated by Django 3.2.4 on 2023-10-02 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sesion',
            fields=[
                ('id_user', models.IntegerField(db_column='idUser', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Nombre', max_length=100)),
                ('email', models.CharField(db_column='Correo', max_length=100)),
                ('pas', models.CharField(db_column='Pass', max_length=100)),
            ],
            options={
                'db_table': 'Ingreso',
            },
        ),
    ]
