from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages


class SignupView(FormView):
    """sign up user view"""
    form_class = forms.SignupForm
    template_name = 'custom_auth/signup.html'
    success_url = reverse_lazy('custom_auth:dashboard')

    def form_valid(self, form):
        """ process user signup
            The default implementation for form_valid() simply redirects to the success_url.
        """
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        login(self.request, user)
        if user is not None:
            return HttpResponseRedirect(self.success_url)
        return super().form_valid(form)


def Dashboard(request):
    """ make dashboard view """
    return render(request, 'custom_auth/dashboard.html')


def Logout(request):
    """logout logged in user"""
    logout(request)
    return HttpResponseRedirect(reverse_lazy('custom_auth:dashboard'))


class LoginView(FormView):
    """login view"""

    form_class = forms.LoginForm
    success_url = reverse_lazy('custom_auth:dashboard')
    template_name = 'custom_auth/login.html'

    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data

        user = authenticate(username=credentials['email'],
                            password=credentials['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect(reverse_lazy('custom_auth:login'))
