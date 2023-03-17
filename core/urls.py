from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

from core.views import index, deposit, packages,successView,logout, contactView
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path("", views.index, name='index'),
    path('deposit/', views.deposit, name='deposit'),
    path('packages/', views.packages, name='packages'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path("contact/", contactView, name="contact"),
    path("success/", successView, name="success"),
    path("inbox", views.inbox, name="inbox"),
    path('profile/', views.profile, name='profile'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="core/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'), name='password_reset_complete'), 
    path("password_reset", views.password_reset_request, name="password_reset")
    # path('withdraw/', views.Withdraw, name="withdraw"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
