import logging
from datetime import datetime

from django.shortcuts import render
from Django_Registration import settings
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.urls import reverse
from django.views.generic import FormView, View
from django.contrib.auth.decorators import login_required
from .forms import *
import logging

# Create your views here.
logger = logging.getLogger(__name__)


# Home Page View
def home(request):
    #logger.warning('Homepage was accessed at ' + str(datetime.now()) + ' hours!')
    logger.warning("ANothing here")
    return render(request, template_name='website/home.html')


def register_new_user(form, request):
    existing_user = User.objects.filter(email=form.cleaned_data['email'])

    if existing_user.exists():
        password_reset_url = request.scheme + '://' + request.get_host() + reverse('password_reset')
        existing_user.first().email_user(
            get_template('emails/already_registered_subject.txt').render(context={'site_name': settings.SITE_NAME}),
            get_template('emails/already_registered.html').render(context={'password_reset_url': password_reset_url}))
        raise IntegrityError("Email already exists: %s" % form.cleaned_data['email'])
    else:
        # Create and log in user
        newly_created_user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'])
        login(request, newly_created_user)


@login_required(login_url='/login')
def UpdateProfileView(request):
    if request.method == "POST":
        query = User.objects.get(id=request.user.id)
        query.first_name = request.POST.get('first_name')
        query.last_name = request.POST.get('last_name')
        query.email = request.POST.get('email')
        query.save()
        context = {'first_name': query.first_name, 'last_name': query.last_name,
                   'email': query.email}
        return render(request, template_name='edit_profile/updated_profile.html', context=context)
    else:
        query = User.objects.get(id=request.user.id)
        context = {'first_name': query.first_name, 'last_name': query.last_name, 'username': query.username,
                   'email': query.email}
        return render(request, template_name='edit_profile/edit_form.html', context=context)


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        try:
            register_new_user(form, self.request)
            messages.success(self.request, 'Thank you for registering. You have been automatically logged in.')
            return HttpResponse(get_template('registration/registration_complete.html').render())
        except IntegrityError as e:
            print("Error when registering a new user: %s" % e)
            return HttpResponse(get_template('registration/registration_complete.html').render())


@login_required
def view(request):
    return render(request, template_name='account/view.html')
