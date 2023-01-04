from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from common.views import TitleMixin
from users.models import User 
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
  

