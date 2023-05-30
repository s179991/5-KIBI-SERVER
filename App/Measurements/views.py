from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from App.settings import SECRET_KEY
from Device.forms import DeviceForm
from Device.models import Device
from .models import Measurement

@csrf_exempt
def DeviceMeasurement(request, T, RH, p, P, O, CO2):
    """Function called when querying http /device/measurement/. Saves the values to the database.

    Args:
        request (HttpRequest): argument contains query data (headers, user, IP address and POST data).
        T (str): Temperature value in Celcius
        RH (str): Relative Humidity in % (0-100)
        p (str): Pressure value in Pa
        P (str): Power consumption in W
        O (str): Oxygen producing
        CO2 (str): CarbonDioxide use value

    Returns:
        HttpResponse: response to the device, containing information about the correctness of the Measurement saving.
    """
    if request.method == "POST":
        form = DeviceForm(request.POST)
        key = form.cleaned_data.get("KEY")
        IPAddress = request.META.get("REMOTE_ADDR")
        if key == SECRET_KEY and Device.IsConnected(IPAddress):
            measurement = Measurement(
                Temperature=T,
                Humidity=RH,
                Pressure=p,
                Power=P,
                Oxygen=O,
                CarbonDioxide=CO2
            )
            measurement.save()
            return HttpResponse(status=200)
    return HttpResponse(status=404)

