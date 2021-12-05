from django.db.models import Q, Sum


def extract(inf):
    pago = inf.filter(Q(pay=True)).aggregate(result=Sum('val'))
    dev = inf.filter(Q(pay=False)).aggregate(result=Sum('val'))
    pago_final = 0 if pago['result'] is None else round(pago['result'], 2)
    dev_final = 0 if dev['result'] is None else round(dev['result'], 2)
    return pago_final, dev_final
