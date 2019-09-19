# Generated by Django 2.2.5 on 2019-09-19 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('count', models.IntegerField()),
                ('game', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('courts', models.IntegerField()),
                ('schedule', models.CharField(max_length=250)),
                ('image_url', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=50)),
                ('homecourt', models.CharField(max_length=50)),
                ('games', models.ManyToManyField(to='main_app.Game')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Park'),
        ),
    ]
