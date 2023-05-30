from django import forms

class DeviceForm(forms.Form):
    """A form with device data, sent using the POST method when connecting and disconnecting the device.

    Base class:
        Form (django.forms): The base class that provides access to the format validation methods.
    """
    KEY = forms.CharField(label="KEY", max_length=64)
    """
        API Key field, maximum length 64 bytes.
    """
    MAC = forms.CharField(label="MAC", max_length=20)
    """
        Device MAC address field, maximum length 20 bytes.
    """
    IP = forms.GenericIPAddressField(label="IP")
    """
        Device IP address field.
    """