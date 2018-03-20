from django.urls import path

from . import views

app_name = 'memberships'
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forget-pass/', views.ForgetPassView.as_view(), name='forget_pass'),
    path('activation/<str:id>/<str:code>', views.ActivationView.as_view(), name='activation'),
    path('reset-code/<str:email>/<str:code>', views.ResetCodeView.as_view(), name='reset_code'),
]
