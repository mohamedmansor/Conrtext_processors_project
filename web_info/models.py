from django.db import models


class Website(models.Model):
    website_name = models.CharField(max_length=50)
    ticker = models.CharField(max_length=1000, default="NEWSFLASH")
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=100, blank=True)
    info = models.TextField(max_length=200, blank=True)
    sales_phone = models.CharField(max_length=200, blank=True)
    bkg_phone = models.CharField(max_length=200, blank=True)
    salse_email_1 = models.EmailField(max_length=30, blank=True)
    salse_email_2 = models.EmailField(max_length=30, blank=True)
    logo = models.ImageField(upload_to="logos")
    