# Generated by Django 3.2.9 on 2021-11-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Agriculture', 'Agriculture'), ('Accounting', 'Accounting'), ('Tresurer', 'Tresurer'), ('MPDC', 'MPDC'), ('MCTC', 'MCTC'), ('MCR', 'MCR'), ('Mayor', 'Mayor'), ('Tourism', 'Tourism')], max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
