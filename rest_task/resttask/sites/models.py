from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class Site(models.Model):

    CHOICES_BOOLEANO_YES_NO = (
        ('yes', 'Yes'),
        ('no', 'No')
    )
    
    def validate_active(value):
        if value in ['yes', 'no']:
            raise ValidationError(
                _('Active must be \"yes\" or \"no\"'),
                params={'value': value},
            )

    name = models.CharField("SiteName",
                            max_length=20, unique=True)
    region = models.CharField("Region", max_length=50)
    latitude = models.FloatField("Latitude", default=0)
    longitude = models.FloatField("Longitude", default=0)
    active = models.CharField(
        max_length=3, choices=CHOICES_BOOLEANO_YES_NO, default='no', validators=[validate_active])
    
    def __str__(self):
        return self.name


class Request(models.Model):

    reuest_no = models.IntegerField(_("Reuest No."))
    details = models.TextField(_("Request Details"))
    site = models.ForeignKey( Site, name="SiteName", on_delete=models.CASCADE)

