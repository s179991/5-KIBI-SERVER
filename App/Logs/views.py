from django.shortcuts import render
from django.http import HttpResponse
from App.settings import SECRET_KEY
from Device.forms import DeviceForm
from Device.models import Device
from .models import Log

def RegisterLog(request, level, text):
    """Function called when querying http /log/level/text/. Saves the Log to the database.

    Args:
        request (HttpRequest): argument contains query data (headers, user, IP address and POST data).

        level   (str): log level (ERR, WAR, INF)

        text    (str): log information

    Returns:
        HttpResponse: response to the device, containing information about the correctness of the Log saving.
    """
    if request.method == "POST":
        form = DeviceForm(request.POST)
        key = form.cleaned_data.get("KEY")
        IPAddress = request.META.get("REMOTE_ADDR")
        if key == SECRET_KEY and Device.IsConnected(IPAddress):
            log = Log(level=level, text=text)
            log.save()
            return HttpResponse(status=200)
    return HttpResponse(status=404)
