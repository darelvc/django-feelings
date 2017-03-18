from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import ThoughtForm


class CreateThought(LoginRequiredMixin, CreateView):
    form_class = ThoughtForm
    success_url = reverse_lazy('users:dashboard')

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
