from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponseRedirect

from . import forms


def dashboard(request):
    return render(request, 'users/dashboard.html')


class LogoutView(FormView):
    form_class = forms.LogoutForm
    template_name = 'users/logout.html'

    def form_valid(self, form):
        logout(self.request)
        return HttpResponseRedirect(reverse('home'))

