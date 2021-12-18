import os
import requests
import json

# Settings
from_zendesk = 'https://newsandrewards.zendesk.com'
from_credentials = 'EMAIL', 'PASSWORD'

to_zendesk = 'https://sliide.zendesk.com'
to_credentials = 'EMAIL_TO', 'PASSWORD'

from_endpoint = from_zendesk + '/api/v2/tickets.json?include=comment_count'

tickets_count = 0

while from_endpoint:
    response = requests.get(from_endpoint, auth=from_credentials)
    if response.status_code != 200:
        print('Failed to retrieve tickets with error {}'.format(response.status_code))
        exit()
    data = response.json()

    for ticket in data['tickets']:
        tickets_count += 1
        print(ticket)

        exit()

    from_endpoint = data['next_page']


print(tickets_count)
        