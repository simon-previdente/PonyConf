from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.http import HttpResponse, Http404

from ponyconf.mixins import OnSiteFormMixin

from accounts.decorators import orga_required, staff_required
from accounts.mixins import OrgaRequiredMixin, StaffRequiredMixin

from proposals.models import Talk

from .models import Room
from .forms import RoomForm
from .utils import Program


class RoomMixin(object):
    def get_queryset(self):
        return Room.objects.filter(site=get_current_site(self.request)).all()


class RoomFormMixin(OnSiteFormMixin):
    form_class = RoomForm


class RoomList(StaffRequiredMixin, RoomMixin, ListView):
    pass


class RoomCreate(OrgaRequiredMixin, RoomMixin, RoomFormMixin, CreateView):
    model = Room

class RoomUpdate(OrgaRequiredMixin, RoomMixin, RoomFormMixin, UpdateView):
    pass

class RoomDetail(StaffRequiredMixin, RoomMixin, DetailView):
    pass


@staff_required
def program_pending(request):
    output = request.GET.get('format', 'html')
    return program(request, pending=True, output=output, html_template='schedule.html', cache=False)


def program_public(request):
    output = request.GET.get('format', 'html')
    return program(request, pending=False, output=output)


def program(request, pending=False, output='html', html_template='public-program.html', cache=True):
    program = Program(site=get_current_site(request), pending=pending, cache=cache)
    if output == 'html':
        return render(request, 'planning/' + html_template, {'program': program.render('html')})
    elif output == 'xml':
        return HttpResponse(program.render('xml'), content_type="application/xml")
    elif output == 'ics':
        return HttpResponse(program.render('ics'), content_type="text/calendar")
    else:
        raise Http404("Format not available")
