from django.db import models
from django.utils import timezone, dateformat
from App.settings import DATE_FORMAT

class Log(models.Model):
    """Database model for device logs.

    Base class:
        Model (django.db.models): The base class that provides access to the format validation methods.
    """
    LEVEL_CHOICE = [
        ("INF", "Information"),
        ("WAR", "Warning"),
        ("ERR", "Error"),
    ]
    """
        Definition of log levels (WAR, INF, ERR)
    """
    level = models.CharField(max_length=3, choices=LEVEL_CHOICE, default="INF", null=False)
    """
        The database log level model contains a maximum length of 3 characters.
    """
    text = models.CharField(max_length=255, null=False)
    """
        The database log information model has a maximum length of 255 characters.
    """
    registration_time = models.DateTimeField(default=timezone.now, null=False)
    """
        Database field with the value of the log registration date.
    """

    @staticmethod
    def Info(text):
        """a method that saves log information at the info level

        Args:
            text (str): log information

        Returns:
            bool: true if success saving in db, otherwise false
        """
        try:
            level = "INF"
            text = str(text)
            log = Log(level=level, text=text)
            log.save()
        except:
            return False
        return True

    @staticmethod
    def Warn(text):
        """a method that saves log information at the warning level

        Args:
            text (str): log information

        Returns:
            bool: true if success saving in db, otherwise false
        """
        try:
            level = "WAR"
            text = str(text)
            log = Log(level=level, text=text)
            log.save()
        except:
            return False
        return True

    @staticmethod
    def Error(text):
        """a method that saves log information at the error level

        Args:
            text (str): log information

        Returns:
            bool: true if success saving in db, otherwise false
        """
        try:
            level = "ERR"
            text = str(text)
            log = Log(level=level, text=text)
            log.save()
        except:
            return False
        return True

    def __str__(self):
        """Method that formats data when viewed in an administrator window.

        Returns:
            str: formated data
        """
        date = dateformat.format(self.registration_time, DATE_FORMAT)
        return f"[{date}] | [{self.level}] -> {self.text}"
