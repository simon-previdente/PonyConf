from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView

from cfp.forms import ProposeForm
from cfp.models import Participant

class ProposeView(FormView):
    form_class = ProposeForm
    template_name = 'cfp/propose.html'
    success_url = reverse_lazy('propose-complete')

    def form_valid(self, form):
        talk = form.talk_form.save(commit=False)
        talk.site = get_current_site(self.request)
        talk.save()
        email = form.participant_form.cleaned_data['email']
        try:
            participant = Participant.objects.get(email=email)
        except Participant.DoesNoExist:
            participant = participant_form.save(commit=False)
            participant.site = get_current_site(self.request)
            participant.save()
        talk.speakers.add(participant)
        return HttpResponseRedirect(self.success_url)


class CompleteView(TemplateView):
    template_name = 'cfp/complete.html'
