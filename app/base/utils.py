from django.http import HttpResponse
from django.template import RequestContext
from django.conf import settings
from django.utils.translation import ugettext as _

from django.shortcuts import render_to_response

def render_response(request, template, context):
    return render_to_response(template, context,
            context_instance=RequestContext(request))

def process_template(request):
    from django.conf import settings
    return {
            'settings': settings,
            'debug': settings.DEBUG,
            'request': request,
            'user': request.user,
            'STATIC_URL': settings.STATIC_URL,
            'LANGUAGE_CODE': request.LANGUAGE_CODE,
        }


class cached_property(object):
    '''A read-only @property that is only evaluated once. The value is cached
    on the object itself rather than the function or class; this should prevent
    memory leakage.'''
    def __init__(self, fget, doc=None):
        self.fget = fget
        self.__doc__ = doc or fget.__doc__
        self.__name__ = fget.__name__
        self.__module__ = fget.__module__

    def __get__(self, obj, cls):
        if obj is None:
            return self
        obj.__dict__[self.__name__] = result = self.fget(obj)
        return result

