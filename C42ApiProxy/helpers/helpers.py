from C42ApiProxy.apis.apis import get_event_details, get_event_subscriptions


def get_event_title(event_id):

    event_info = get_event_details(event_id)

    if event_info.get('error'):
        title = 'There was an error getting the title'
    else:
        title = event_info.get('data')[0].get('title')

    return title


def get_event_names(event_id):

    event_info = get_event_subscriptions(event_id)

    if event_info.get('error'):
        names = 'There was an error getting the names'
    else:
        names = []
        for dict in event_info.get('data'):
            names.append(str(dict.get('subscriber').get('first_name')))

    return names
