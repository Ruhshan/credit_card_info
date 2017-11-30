from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=127, verbose_name="Name ")
    status = models.BooleanField(default=True)
    circuit_id = models.IntegerField(verbose_name="Circuit ID ")
    earning_per_share = models.DecimalField(decimal_places=3, max_digits=10, verbose_name="Earnings Per Share ")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class BankDetails(models.Model):
    about = models.TextField(blank=True, verbose_name="About ")
    email = models.EmailField(blank=True, verbose_name="Email ")
    phone = models.CharField(blank=True, max_length=50, verbose_name="Phone Number ")
    camels = models.CharField(max_length=50, verbose_name="CAMELS ")
    address = models.TextField(blank=True, verbose_name="Address ")
    registered = models.CharField(max_length=50, blank=True, verbose_name="Registered ")
    bank = models.OneToOneField(Bank, verbose_name="Details", null=True, blank=True, related_name="details")

class OperatingHour(models.Model):
    DAY_CHOICES = (('suday', 'sunday'),
                   ('monday', 'monday'),
                   ('tuesday', 'tuesday'),
                   ('wednesday', 'wednesday'),
                   ('thursday', 'thursday'),)
    day = models.CharField(max_length=30, choices=DAY_CHOICES, verbose_name="Day ")
    start = models.TimeField(verbose_name="Start ")
    end = models.TimeField(verbose_name="End ")
    details = models.ForeignKey(BankDetails, verbose_name="Operating Hours ", related_name="operating_hours")

class Branch(models.Model):
    bank = models.ForeignKey(Bank, verbose_name="Bank ")
    name = models.CharField(max_length=127, verbose_name="Branch Name ")
    address = models.TextField(verbose_name="Branch Address")

    def __str__(self):
        return "{} , {} Branch".format(self.bank.name, self.name)

    class Meta:
        verbose_name_plural = "Branches"


class AtmBooth(models.Model):
    bank = models.ForeignKey(Bank, verbose_name="Bank ", related_name="atm_booths")
    name = models.CharField(max_length=127, verbose_name="ATM Name ")
    status = models.BooleanField(default=True, verbose_name= "Status ")
    location = JSONField(verbose_name="Location ")

    def __str__(self):
        return "{} , {} ATM".format(self.bank.name, self.name)

