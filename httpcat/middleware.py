from django.http import HttpResponse
from django.conf import settings

OK_CODES = getattr(settings, "HTTP_OK_CODES", [200, 304])

class HttpCatErrorHandler(object):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_response(self, request, response):
        if response.status_code not in OK_CODES:
            url = "https://http.cat/" + str(response.status_code)
            return HttpResponse('<img src="{0}">'.format(url), status=response.status_code)
        return response
