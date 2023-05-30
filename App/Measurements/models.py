from django.db import models
from django.utils import timezone, dateformat
from App.settings import DATE_FORMAT

class Measurement(models.Model):
    """Database model for Measurements.

    Base class:
        Model (django.db.models): The base class that provides access to the format validation methods.
    """
    Humidity = models.CharField(max_length=20, null=False)
    """
        Field to save RH value
    """
    CarbonDioxide = models.CharField(max_length=20, null=False)
    """
        Field to save CO2 value
    """
    Oxygen = models.CharField(max_length=20, null=False)
    """
        Field to save O2 value
    """
    Temperature = models.CharField(max_length=20, null=False)
    """
        Field to save T value
    """
    Pressure = models.CharField(max_length=20, null=False)
    """
        Field to save p value
    """
    Power = models.CharField(max_length=20, null=False)
    """
        Field to save P value
    """
    registration_time = models.DateTimeField(default=timezone.now, null=False)
    """
        Field to save measurement registration time
    """

    def __str__(self):
        """Method that formats data when viewed in an administrator window.

        Returns:
            str: formated data
        """
        date = dateformat.format(self.registration_time, DATE_FORMAT)
        str  = f"Values: "
        str += f"Temperature: {self.Temperature} °C, "
        str += f"RH {self.Humidity}%, "
        str += f"Pressure: {self.Pressure} Pa, "
        str += f"Oxygen: {self.Oxygen}%, "
        str += f"CO2: {self.CarbonDioxide}%, "
        str += f"Power: {self.Power} W "
        str += f"-> at time {date}"
        return str

