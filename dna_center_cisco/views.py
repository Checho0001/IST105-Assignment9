from django.shortcuts import render
from .utils.dnac import DNAC_Manager
from .models import InteractionLog

dnac = DNAC_Manager()

def auth_view(request):
    result = dnac.get_auth_token(display_token=False)
    InteractionLog.objects.create(
        ip_address='N/A',
        result='success' if result else 'failure',
        action='token'
    )
    return render(request, "auth_token.html", {"token": dnac.token if result else None})


def devices_view(request):
    devices = dnac.get_network_devices()
    InteractionLog.objects.create(
        ip_address='N/A',
        result='success' if devices else 'failure',
        action='list_devices'
    )
    return render(request, "devices.html", {"devices": devices})


def interfaces_view(request):
    ip = request.GET.get("ip")
    interfaces = dnac.get_device_interfaces(ip)
    InteractionLog.objects.create(
        ip_address=ip or "N/A",
        result='success' if interfaces else 'failure',
        action='show_interfaces'
    )
    return render(request, "interfaces.html", {"interfaces": interfaces, "ip": ip})
