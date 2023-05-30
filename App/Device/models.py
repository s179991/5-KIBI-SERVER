from django.db import models
from django.utils import timezone, dateformat
from django.http import HttpRequest
from App.settings import DATE_FORMAT, DEVICE_TOKEN
from .forms import DeviceForm

class Device(models.Model):
    """Database model for connected devices.

    Base class:
        Model (django.db.models): The base class that provides access to the format validation methods.
    """
    IP = models.GenericIPAddressField()
    """
        IP address of device
    """
    MAC = models.CharField(max_length=20, null=True)
    """
        MAC address of device
    """
    connected_time = models.DateTimeField(default=timezone.now)
    """
        Device connection time
    """

    @staticmethod
    def Auth(request: HttpRequest):
        """Device authorization function, checks the correctness of data sent via POST by device.

        Args:
            request (HttpRequest): argument contains query data (headers, user, IP address and POST data).

        Returns:
            bool, str, str: returns 3 values, authorization success, and the IP and MAC address of the device.
        """
        if request.method == "POST":
            form = DeviceForm(request.POST)
            if form.is_valid():
                key = form.cleaned_data.get("KEY")
                IPAddress = form.cleaned_data.get("IP")
                MACAddress = form.cleaned_data.get("MAC")
                if key == DEVICE_TOKEN:
                    return True, IPAddress, MACAddress
        return False, "", ""
    
    @staticmethod
    def Disconnect():
        """
            Method disconnects the devices from the database.
        """
        cnt = Device.objects.all().count()
        if cnt > 0:
            Device.objects.all().delete()

    @staticmethod
    def Connect(IPAddress, MACAddress):
        """Method connects the device to the database.

        Args:
            IPAddress (str): the IP address of the device to be connected
            MACAddress (str): the MAC address of the device to be connected
        """
        Device.Disconnect()
        device = Device(IP=IPAddress, MAC=MACAddress)
        device.save()

    @staticmethod
    def IsConnected(IPAddress):
        """Method checks the connection status of the device by indicated IP address.

        Args:
            IPAddress (str): the IP address of the device to be check

        Returns:
            bool: true if connected, otherwise false
        """
        if Device.objects.all().count() == 1 and Device.objects.filter(IP=IPAddress).count() == 1:
            return True
        return False
    
    def IsConnected(self):
        """Method checks the connection status of the device instance

        Returns:
            bool: true if connected, otherwise false
        """
        if Device.objects.all().count() == 1:
            return True
        return False

    def __str__(self):
        """Method that formats data when viewed in an administrator window.

        Returns:
            str: formated data
        """
        date = dateformat.format(self.connected_time, DATE_FORMAT)
        return f"IP: {self.IP}, connected at {date}"


