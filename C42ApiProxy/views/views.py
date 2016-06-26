from django.shortcuts import render
from django.views.decorators.cache import cache_page

from C42ApiProxy.helpers.helpers import get_event_title, get_event_names


@cache_page(252, cache='default')
def index(request):

    event_id = request.path.split('/')[2]

    title = get_event_title(event_id)
    names = get_event_names(event_id)

    response_dict = {
        "id": event_id,
        "title": title,
        "names": names
    }

    return render(request, 'index.html', {'response_dict': response_dict})
