# Generated by Django 3.0.2 on 2020-07-25 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(choices=[('Coding Club', 'Coding Club IITG'), ('Electronics', 'Electroncis Club IITG'), ('Robotics', 'Robotics Club IITG'), ('LitSoc', 'Literary Society IITG'), ('Xpressions', 'Drama Club IITG'), ('Aeromodelling', 'Aeromodelling Club IITG'), ('Cadence', 'Dance Club IITG'), ('IITG.AI', 'Artificial intelligence Club IITG')], max_length=50)),
                ('secretary', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=30)),
                ('updated_on', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('club_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.Club')),
            ],
        ),
    ]