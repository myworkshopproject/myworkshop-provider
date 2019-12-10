from django.conf import settings
from django.urls import path, include

app_name = "accounts"


from accounts.views import ProfileJSONView


urlpatterns = [path("profile/", ProfileJSONView, name="profile_json")]
