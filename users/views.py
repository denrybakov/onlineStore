from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView

from common.views import TitleMixin
from users.models import User, EmailVerification
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket

# Create views
class UserLoginView(TitleMixin, LoginView):
  template_name = 'users/login.html'
  form_class = UserLoginForm
  success_url = reverse_lazy('index')
  title = 'Store - Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
  model = User
  form_class = UserRegistrationForm
  template_name = 'users/register.html'
  success_url = reverse_lazy('users:login')
  success_message = 'Вы успешно зарегистрированы'
  title = 'Store - Регистрация'


class UserProfileView(TitleMixin, UpdateView):
  model = User 
  form_class = UserProfileForm
  template_name = 'users/profile.html'
  title = 'Store - Профиль'

  def get_success_url(self):
    return reverse_lazy('users:profile', args=(self.object.id,))

  def get_context_data(self, **kwargs):
    context = super(UserProfileView, self).get_context_data()
    context['baskets'] = Basket.objects.filter(user=self.object)
    return context
  

class EmailVerificationView(TitleMixin, TemplateView):
  title = 'Store - Подтверждение электронной почты'
  template_name = 'users/email_verification.html'

  def get(self, request, *args, **kwargs):
    code = kwargs['code']
    user = User.objects.get(email=kwargs['email']) 
    email_verifications = EmailVerification.objects.filter(user=user, code=code)
    if email_verifications.exists() and not email_verification.first().is_expired():
      user.is_verified_email = True 
      user.save()
      return super(EmailVerificationView, self).get(request, *args, **kwargs)
    else: 
      return HttpResponseRedirect(reverse('index'))
