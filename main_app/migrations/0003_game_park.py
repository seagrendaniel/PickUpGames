from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20190916_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('courts', models.IntegerField()),
                ('space', models.CharField(max_length=100)),
                ('schedule', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('count', models.IntegerField()),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.Park')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
