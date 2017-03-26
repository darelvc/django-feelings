from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from .. import forms

from braces.views import SetHeadlineMixin


class Create(LoginRequiredMixin, SetHeadlineMixin, generic.CreateView):
    form_class = forms.FamilyForm
    headline = 'Create a new Family'
    template_name = 'families/form.html'
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response


class Update(LoginRequiredMixin, SetHeadlineMixin, generic.UpdateView):
    form_class = forms.FamilyForm
    template_name = 'families/form.html'

    def get_queryset(self):
        return self.request.user.families.all()

    def get_headline(self):
        return f'Edit {self.object.name}'

    def get_success_url(self):
        return reverse('groups:families:detail', kwargs={'slug': self.object.slug})


class Detail(LoginRequiredMixin, generic.UpdateView):
    form_class = forms.FamilyForm
    template_name = 'families/detail.html'
    success_url = reverse_lazy('users:dashboard')

    def get_queryset(self):
        return self.request.user.families.all()
