# Generated by Django 4.1.2 on 2022-11-01 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
        ('Employee', '0001_initial'),
        ('Admin', '0001_initial'),
        ('Patients', '0002_claim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Employee.mem_registration'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='consultancy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hospital.consultancy_registration'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.hos_registration'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Employee.mem_registration'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='consultancy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hospital.consultancy_registration'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hospital.doctor_registration'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.hos_registration'),
        ),
    ]
