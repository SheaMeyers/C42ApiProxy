import json

from django.http import HttpResponse


def index(request):

    response_dict = {
        "id": "$EVENT_ID",
        "title": "Test Event",
        "names": ["Bob", "Ella"]
    }

    return HttpResponse(json.dumps(response_dict))
