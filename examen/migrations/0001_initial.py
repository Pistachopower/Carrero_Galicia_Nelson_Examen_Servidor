# Generated by Django 5.1.2 on 2024-11-05 09:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
                ('anio_estreno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('direccion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_alquiler', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alquileres', to='examen.pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alquileres_usuario', to='examen.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='pelicula',
            name='usuario',
            field=models.ManyToManyField(related_name='peliculas_alquiladas', through='examen.Alquiler', to='examen.usuario'),
        ),
        migrations.CreateModel(
            name='CuentaBancaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cuenta', models.CharField(max_length=20)),
                ('banco', models.CharField(choices=[('Caixa', 'Caixa'), ('BBVA', 'BBVA'), ('UNICAJA', 'Unicaja'), ('ING', 'ING')], max_length=8)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cuenta_bancaria', to='examen.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.CharField(choices=[('1', 'Uno'), ('2', 'Dos'), ('3', 'Tres'), ('4', 'Cuatro'), ('5', 'Cinco')], max_length=1)),
                ('comentario', models.TextField()),
                ('fecha_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votos', to='examen.pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votos_usuario', to='examen.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='pelicula',
            name='voto',
            field=models.ManyToManyField(related_name='peliculas_votadas', through='examen.Voto', to='examen.usuario'),
        ),
    ]
