

from django.http import HttpResponseBadRequest
from .http_helpers import is_hx_request

def hx_required(func):
    def wrap(request , *args, **kwargs):
        if not is_hx_request(request):
            return HttpResponseBadRequest("hx request required")
        return func(request,*args, **kwargs)
    wrap.__doc__ = func.__doc__
    wrap.__name__  = func.__name__
    return wrap