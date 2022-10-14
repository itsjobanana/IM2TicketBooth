# Generated by Django 4.1.2 on 2022-10-14 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingC',
            fields=[
                ('bookingID', models.AutoField(primary_key=True, serialize=False)),
                ('numberOfSeats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookingM',
            fields=[
                ('bookingID', models.AutoField(primary_key=True, serialize=False)),
                ('numberOfSeats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('concertID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=50)),
                ('concertDate', models.DateField()),
                ('timeStart', models.TimeField()),
                ('seatType', models.CharField(choices=[('V', 'VIP'), ('R', 'Regular')], max_length=10)),
                ('price', models.FloatField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('dateAvailable', models.DateField()),
                ('timeAired', models.TimeField()),
                ('roomType', models.CharField(choices=[('V', 'VIP'), ('R', 'Regular')], max_length=1)),
                ('price', models.IntegerField(choices=[('500', '500'), ('1000', '1000')], max_length=100)),
                ('capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('U', 'User'), ('A', 'Admin')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='registration.user')),
                ('admincode', models.CharField(max_length=10)),
            ],
            bases=('registration.user',),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='registration.user')),
                ('address', models.CharField(max_length=50)),
            ],
            bases=('registration.user',),
        ),
        migrations.CreateModel(
            name='TicketM',
            fields=[
                ('ticketID', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('bookingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.bookingm')),
            ],
        ),
        migrations.CreateModel(
            name='TicketC',
            fields=[
                ('ticketID', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('bookingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.bookingc')),
            ],
        ),
        migrations.CreateModel(
            name='CancelM',
            fields=[
                ('dateCancelled', models.DateField(primary_key=True, serialize=False)),
                ('reason', models.CharField(max_length=100)),
                ('ticketID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.ticketm')),
            ],
        ),
        migrations.CreateModel(
            name='CancelC',
            fields=[
                ('dateCancelled', models.DateField(primary_key=True, serialize=False)),
                ('reason', models.CharField(max_length=100)),
                ('ticketID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.ticketc')),
            ],
        ),
        migrations.AddField(
            model_name='bookingm',
            name='movieID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.movie'),
        ),
        migrations.AddField(
            model_name='bookingc',
            name='concertID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.concert'),
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.admin')),
            ],
            options={
                'unique_together': {('admin', 'specialization')},
            },
        ),
    ]
