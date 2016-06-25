from django.shortcuts import render


def index(request):

    event_id = request.path.split('/')[2]

    response_dict = {
        "id": event_id,
        "title": "Test Event",
        "names": ["Bob", "Ella"]
    }

    return render(request, 'index.html', {'response_dict': response_dict})