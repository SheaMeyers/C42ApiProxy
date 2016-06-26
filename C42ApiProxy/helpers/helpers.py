from C42ApiProxy.apis.apis import get_event_details, get_event_subscriptions


def get_event_title(event_id):
    """
    Gets the title of the event
    :param event_id: The event id
    :return: success: The title of the event as a string
             error: An error message as a string
    """
    event_info = get_event_details(event_id)

    if event_info.get('error'):
        title = 'There was an error getting the title'
    else:
        title = event_info.get('data')[0].get('title')

    return title


def get_event_names(event_id):
    """
    Gets the names of the subscribers of the event
    :param event_id: The event id
    :return: success: The names of the event subscribers in a list
             error: An error message is a list
    """
    event_info = get_event_subscriptions(event_id)

    if event_info.get('error'):
        names = ['There was an error getting the names']
    else:
        names = []
        for dict in event_info.get('data'):
            names.append(str(dict.get('subscriber').get('first_name')))

    return names
