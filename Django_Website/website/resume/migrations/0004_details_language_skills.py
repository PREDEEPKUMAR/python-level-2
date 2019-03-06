# Generated by Django 2.1.7 on 2019-03-03 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resume', '0003_auto_20190303_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('designation', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=200)),
                ('expertise', models.CharField(max_length=50)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Details')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200)),
                ('percentage', models.CharField(max_length=50)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Details')),
            ],
        ),
    ]
