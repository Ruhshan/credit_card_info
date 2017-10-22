from django.core.validators import FileExtensionValidator
from django.db import models
import os
from datetime import datetime


import pandas as pd
# Create your models here.


class CreditCardManager(models.Manager):
    def get_queryset(self):
        return super(CreditCardManager, self).get_queryset()

    def populate_form_csv(self, csv_file):

        df = pd.DataFrame(pd.read_csv(str(csv_file.name), header=0))

        for index, row in df.iterrows():
            print(row['NID'], row[1])

            self.get_or_create(national_id=row[0], name_on_card=row[1], card_number=row[2], expire_on=datetime.strptime(str(row[3]),'%d/%m/%y'),
                        card_cif=row[4], card_cvv=row[5], bank_cif=row[6])



class CreditCard(models.Model):
    national_id = models.CharField(max_length=13, verbose_name="National ID")
    name_on_card = models.CharField(max_length=127, verbose_name="Name On card")
    card_number = models.CharField(max_length=127, verbose_name="Card Number")
    expire_on = models.DateField(verbose_name="Expire On")
    card_cif = models.CharField(max_length=127, verbose_name="Card CIF")
    card_cvv = models.CharField(max_length=127, verbose_name="CVV")
    bank_cif = models.CharField(max_length=127, verbose_name="Bank CIF")

    objects = CreditCardManager()

    def __unicode__(self):
        return self.name_on_card

class FileUpload(models.Model):
    file_name=models.CharField(max_length=127, verbose_name="File Name", null=True, blank=True)
    csv_file = models.FileField(upload_to='uploads/', validators=[FileExtensionValidator(allowed_extensions=['csv'])], verbose_name="File")
    uploaded_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __unicode__(self):
        return self.file_name

    def filename(self):
        return os.path.basename(self.csv_file.name)

    def save(self, *args, **kwargs):
        self.file_name = self.filename()
        super(FileUpload, self).save(*args, **kwargs)
        CreditCard.objects.populate_form_csv(self.csv_file)
