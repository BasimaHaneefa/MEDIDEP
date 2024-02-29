# Generated by Django 4.1.2 on 2022-10-31 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DR_Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avail_fromTime', models.TimeField()),
                ('avail_toTime', models.TimeField()),
                ('avail_date', models.DateField()),
                ('consultancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.consultancy_registration')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor_registration')),
            ],
        ),
        migrations.CreateModel(
            name='GenarateToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_no', models.CharField(max_length=50)),
                ('Token_Booking_status', models.IntegerField(default=0)),
                ('Dr_availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Consultancy.dr_availability')),
            ],
        ),
    ]