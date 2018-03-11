from django.urls import path

from . import views

app_name = 'memberships'
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='registration'),
]
