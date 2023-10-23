from django.urls import path, include, re_path
from dj_rest_auth.views import PasswordResetConfirmView
from accounts.views import CustomEmailConfirmView


urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path(
        "password/reset/confirm/<str:uidb64>/<str:token>",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    re_path(
        r"^registration/account-confirm-email/(?P<key>[-:\w]+)/$",
        CustomEmailConfirmView.as_view(),
        name="account_confirm_email",
    ),
    path("registration/", include("dj_rest_auth.registration.urls")),
]
