from django.http import HttpResponse
from django.utils.translation import ugettext as _

def home(request):
    return HttpResponse(_('Hello'))
