from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
    path("password_change/", auth_view.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_view.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password_reset/", auth_view.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_view.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("register/", views.register, name="register"),
    path("verify/", views.verify_register, name="verify"),
    path("resend/", views.resend_sms, name="resend"),
    path("follow/", views.user_follow, name="follow"),
    path("<str:username>/", views.dashboard, name="profile"),
]
