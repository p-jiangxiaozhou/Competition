from django.conf import settings


def setting(request):
    return {'STATIC_URL': settings.STATIC_URL, 'DOMAIN_URL': settings.DOMAIN_URL}
