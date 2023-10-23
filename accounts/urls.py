from django.urls import path, include, re_path

from accounts.views import CustomEmailConfirmView


urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    re_path(
        r"^registration/account-confirm-email/(?P<key>[-:\w]+)/$",
        CustomEmailConfirmView.as_view(),
        name="account_confirm_email",
    ),
    path("registration/", include("dj_rest_auth.registration.urls")),
]
