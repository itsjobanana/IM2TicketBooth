# Generated by Django 4.1 on 2022-10-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketc',
            name='total',
        ),
        migrations.RemoveField(
            model_name='ticketm',
            name='total',
        ),
        migrations.AlterField(
            model_name='concert',
            name='artist',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='capacity',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='concertName',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='price',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='seatType',
            field=models.CharField(choices=[('V', 'VIP'), ('R', 'Regular')], max_length=1, unique=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='venue',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
