from C42ApiProxy.apis.apis import get_event_details, get_event_subscriptions


def get_event_title(event_id):

    event_info = get_event_details(event_id)

    title = event_info.get('data')[0].get('title')

    return title


def get_event_names(event_id):

    event_info = get_event_subscriptions(event_id)

    names = []
    for dict in event_info.get('data'):
        names.append(str(dict.get('subscriber').get('first_name')))

    return names