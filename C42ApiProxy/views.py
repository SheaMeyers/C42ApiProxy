import json

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    response_dict = {
        "id": "$EVENT_ID",
        "title": "Test Event",
        "names": ["Bob", "Ella"]
    }

    return render(request, 'global.html', {'response_dict': response_dict})