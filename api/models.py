from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    specialization = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, related_name="doctors"
    )

    # Location:
    latitude = models.FloatField()
    longitude = models.FloatField()

    # Availability:
    available_days = models.CharField(max_length=100)
    available_times = models.CharField(max_length=100)

    likes = models.IntegerField(default=0)

    def like(self):
        self.likes += 1
        self.save()

    def unlike(self):
        self.likes -= 1
        self.save()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="appointments"
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name} - {self.appointment_date} {self.appointment_time}"
