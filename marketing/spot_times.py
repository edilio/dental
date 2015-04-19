from django.utils import timezone
from .models import SpotTime


def guess_vehicle(now=None):
    """
    :param now: so it can will be easy to test
    :return:
    """
    if now is None:
        now = timezone.now()
    spot_times = SpotTime.objects.filter(air_time__lte=now).order_by('-air_time')
    try:
        spot_time = spot_times[0]
        return spot_time.vehicle
    except IndexError:
        return None