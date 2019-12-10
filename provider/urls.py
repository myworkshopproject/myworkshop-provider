from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
import oauth2_provider.views as oauth2_views

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    url(r"^authorize/$", oauth2_views.AuthorizationView.as_view(), name="authorize"),
    url(r"^token/$", oauth2_views.TokenView.as_view(), name="token"),
    url(
        r"^revoke-token/$", oauth2_views.RevokeTokenView.as_view(), name="revoke-token"
    ),
]


urlpatterns = [
    path("", include("core.urls")),
    path("accounts/", include("accounts.urls")),
    url(r"^accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    url(r"^o/", include(oauth2_endpoint_views)),
]
