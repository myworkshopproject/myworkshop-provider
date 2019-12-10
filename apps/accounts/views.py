import json
from django.http import HttpResponse
from oauth2_provider.decorators import protected_resource


@protected_resource(scopes=["read"])
def ProfileJSONView(request):
    return HttpResponse(
        json.dumps(
            {
                "id": str(request.resource_owner.id),
                "username": request.resource_owner.username,
                "email": request.resource_owner.email,
                "first_name": request.resource_owner.first_name,
                "last_name": request.resource_owner.last_name,
            }
        ),
        content_type="application/json",
    )
