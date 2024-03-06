# Generated by Django 4.2.7 on 2024-02-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=10)),
                ('coordinate', models.CharField(max_length=20)),
                ('temperature', models.DecimalField(decimal_places=5, max_digits=10)),
                ('pressure', models.DecimalField(decimal_places=5, max_digits=10)),
                ('humidity', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]
