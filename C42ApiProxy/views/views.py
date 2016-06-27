from django.shortcuts import render
from django.views.decorators.cache import cache_page

from C42ApiProxy.helpers.helpers import get_event_title, get_event_names


# Cache page for 4.2 minutes in the 'default' cache
@cache_page(252, cache='default')
def index(request, event_id):
    """
    Renders an html page for the request a user makes
    :param request: The request a user names
    :param event_id: The id of the event
    :return: A rendered html page with the event id, event title, and event names
    """
    title = get_event_title(event_id)
    names = get_event_names(event_id)

    response_dict = {
        "id": event_id,
        "title": title,
        "names": names
    }

    return render(request, 'index.html', {'response_dict': response_dict})
