# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Adr(models.Model):

    #__Adr_FIELDS__
    number = models.IntegerField(null=True, blank=True)

    #__Adr_FIELDS__END

    class Meta:
        verbose_name        = _("Adr")
        verbose_name_plural = _("Adr")


class Freight(models.Model):

    #__Freight_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Freight_FIELDS__END

    class Meta:
        verbose_name        = _("Freight")
        verbose_name_plural = _("Freight")


class Body(models.Model):

    #__Body_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Body_FIELDS__END

    class Meta:
        verbose_name        = _("Body")
        verbose_name_plural = _("Body")


class Permit(models.Model):

    #__Permit_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Permit_FIELDS__END

    class Meta:
        verbose_name        = _("Permit")
        verbose_name_plural = _("Permit")


class Specialequipment(models.Model):

    #__Specialequipment_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Specialequipment_FIELDS__END

    class Meta:
        verbose_name        = _("Specialequipment")
        verbose_name_plural = _("Specialequipment")


class Countryinformation(models.Model):

    #__Countryinformation_FIELDS__
    country = models.CharField(max_length=255, null=True, blank=True)
    calling_code = models.IntegerField(null=True, blank=True)
    currency_code = models.CharField(max_length=255, null=True, blank=True)

    #__Countryinformation_FIELDS__END

    class Meta:
        verbose_name        = _("Countryinformation")
        verbose_name_plural = _("Countryinformation")


class Carrier(models.Model):

    #__Carrier_FIELDS__
    company_name = models.CharField(max_length=255, null=True, blank=True)
    tax_number = models.CharField(max_length=255, null=True, blank=True)
    responsible_person_name = models.CharField(max_length=255, null=True, blank=True)
    primary_phone = models.CharField(max_length=255, null=True, blank=True)
    details = models.TextField(max_length=255, null=True, blank=True)
    freight_type = models.ForeignKey(Freight, on_delete=models.CASCADE)
    body_type = models.ForeignKey(Body, on_delete=models.CASCADE)
    countries = models.ForeignKey(CountryInformation, on_delete=models.CASCADE)
    have_adr = models.BooleanField()
    adr = models.ForeignKey(Adr, on_delete=models.CASCADE)
    maybe_have_adr = models.BooleanField()
    special_equipment = models.ForeignKey(SpecialEquipment, on_delete=models.CASCADE)
    permit = models.ForeignKey(Permit, on_delete=models.CASCADE)

    #__Carrier_FIELDS__END

    class Meta:
        verbose_name        = _("Carrier")
        verbose_name_plural = _("Carrier")



#__MODELS__END
