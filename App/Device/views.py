from http import HTTPStatus
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from App.settings import DEVICE_TOKEN, CONNECTION_TRACKING_STOP_EVENT
from App.ConnectionTracking import ConnectionTracking
from Logs.models import Log
from .models import *
from .forms import *
           


@csrf_exempt
def DeviceConnect(request):
    """Function called with http /connected request. It checks the correctness of data in the POST method and authorizes the device by saving it in the database.

    Args:
        request (HttpRequest): argument contains query data (headers, user, IP address and POST data).

    Returns:
        HttpResponse: response to the device, containing information about the correctness of the connection to the API.
    """    
    if request.method == "POST":
        success, IPAddress, MACAddress = Device.Auth(request)
        if success:
            Device.Connect()
            Log.Info(f"Connected device from IP '{IPAddress}' and MAC '{MACAddress}'")
            ConnectionTracking(IPAddress, MACAddress)
            return HttpResponse(status=HTTPStatus.ACCEPTED)
    return HttpResponse(status=HTTPStatus.UNAUTHORIZED)
    
    
@csrf_exempt
def DeviceDisconnect(request):
    """Function called with http /disconnected request. It checks the correctness of data in the POST method and authorizes the device by removing it in the database.

    Args:
        request (HttpRequest): argument contains query data (headers, user, IP address and POST data).

    Returns:
        HttpResponse: response to the device, containing information about the correctness of the connection to the API.
    """ 
    if request.method == "POST":
        success, IPAddress, MACAddress = Device.Auth(request)
        if success:
            Device.Disconnect()
            Log.Info(f"Disconnected device from IP '{IPAddress}', MAC '{MACAddress}'")
            # ConnectionTracking(IPAddress, MACAddress)
            return HttpResponse(status=HTTPStatus.ACCEPTED)
    return HttpResponse(status=HTTPStatus.UNAUTHORIZED)