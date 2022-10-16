from django.db import models

# Create your models here.

class User(models.Model):
    type_user = (('U', 'User'), ('A', 'Admin'))
    username = models.CharField(max_length=15, null=False, primary_key=True)
    password = models.CharField(max_length=10, null=False)
    firstname = models.CharField(max_length=50, null=False)
    middlename = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=1, choices=type_user)

    def __str__(self):
        return self.username +' '+ self.firstname + ' '+self.lastname +' '+self.type


class Customer(User):
    address = models.CharField(max_length=50, null=False)


class Admin(User):
    admincode = models.CharField(max_length=10, null=False)

    def __str__(self):
        self.firstname +" "+self.lastname


class Specialization(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)

    class Meta:
        unique_together = ('admin', 'specialization')


class Concert(models.Model):
    type_seat = (('V', 'VIP'), ('R', 'Regular'))
    concertID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    venue = models.CharField(max_length=50, null=False)
    concertDate = models.DateField()
    timeStart = models.TimeField()
    seatType = models.CharField(max_length=10, choices=type_seat)
    price = models.FloatField(null=False)
    capacity = models.IntegerField(null=False)


class Movie(models.Model):
    movieID = models.AutoField(primary_key=True)
    type_room = type_room = (('V', 'VIP'), ('R', 'Regular'))
    title = models.CharField(max_length=50, null=False)
    roomNum = (('1', 'Room1'), ('2', 'Room2'), ('3', 'Room3'), ('4', 'Room4'), ('5', 'Room5'))
    dateAvailable = models.DateField()
    timeAired = models.TimeField()
    roomType = models.CharField(max_length=1, choices=type_room)
    price = models.IntegerField(null=False)
    capacity = models.IntegerField(default=0, null=False)


class BookingM(models.Model):
    bookingID = models.AutoField(primary_key=True)
    numberOfSeats = models.IntegerField(null=False)
    movieID = models.ForeignKey(Movie, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Booking ID: ' + str(self.bookingID)


class BookingC(models.Model):
    bookingID = models.AutoField(primary_key=True)
    numberOfSeats = models.IntegerField(null=False)
    concertID = models.ForeignKey(Concert, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Booking ID: ' + str(self.bookingID)


class TicketM(models.Model):
    ticketID = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    bookingID = models.ForeignKey(BookingM, on_delete=models.CASCADE)


class TicketC(models.Model):
    ticketID = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    bookingID = models.ForeignKey(BookingC, on_delete=models.CASCADE)


class CancelM(models.Model):
    dateCancelled = models.DateField(primary_key=True)
    reason = models.CharField(max_length=100, null=False)
    ticketID = models.ForeignKey(TicketM, on_delete=models.CASCADE)


class CancelC(models.Model):
    dateCancelled = models.DateField(primary_key=True)
    reason = models.CharField(max_length=100, null=False)
    ticketID = models.ForeignKey(TicketC, on_delete=models.CASCADE)

