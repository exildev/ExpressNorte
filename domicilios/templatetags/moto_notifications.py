from datetime import date, timedelta
from django import template
from domicilios.models.motorizado import Moto


register = template.Library()


@register.assignment_tag
def has_exprired(mode):
    # Mixin tag method
    today = date.today()
    # Five days before
    this_date_plus_five_days = today + timedelta(days=5)

    expired_soat = Moto.objects.filter(soat__fecha_expiracionS__range = [today, this_date_plus_five_days])
    expired_tecno = Moto.objects.filter(tecno__fecha_expiracionT__range = [today, this_date_plus_five_days])

    prox_expired_soat = expired_soat.exists()
    prox_expired_tecno = expired_tecno.exists()

    # If just for check
    if mode == "check":
        if prox_expired_soat | prox_expired_tecno:
            return True
        return False
    # Reuse in the view for retrieve the objects dic
    elif mode == "get":
        return {'expired_soat': expired_soat, 'expired_tecno': expired_tecno}
