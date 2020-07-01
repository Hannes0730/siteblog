from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import RegiterPage, EditProfileForm, PasswordEdit

# Create your views here.
class Register(generic.CreateView):
    form_class = RegiterPage
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UpdateProfile(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class ChangePassword(PasswordChangeView):
    form_class = PasswordEdit
    success_url = reverse_lazy('password_success')


def password_sucess(request):
    return render(request, 'registration/password_success.html', {})
