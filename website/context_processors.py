from web_info.models import Website


def website(request):
    return {
        'site': Website.objects.first()
    }
