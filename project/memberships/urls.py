from django.urls import path

from . import views

app_name = 'memberships'
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reset-code/<str:email>/<str:code>', views.ResetCodeView.as_view(), name='reset_code'),
]
