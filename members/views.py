from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,  UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpFrom, EditProfileform


# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileform
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
