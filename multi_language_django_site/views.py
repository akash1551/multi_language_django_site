from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response


def home(request):
    print request.META
    print _('Hello')
    return HttpResponse(_('Hello'))

def index(request):
    return render_to_response('html_templates/index.html')
