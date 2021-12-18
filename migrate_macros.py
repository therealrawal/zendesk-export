import os
import requests
import json

# Settings
from_zendesk = 'https://qlixar.zendesk.com'
from_credentials = 'EMAIL', 'PASSWORD'

to_zendesk = 'https://sliide.zendesk.com'
to_credentials = 'EMAIL', 'PASSWORD'

def get_group_id_by_name(group_name):

    groups_url = to_zendesk + '/api/v2/groups.json'
    response = requests.get(groups_url, auth=to_credentials)

    if response.status_code != 200:
        print('Failed to retrieve articles with error {}'.format(response.status_code))
        exit()
    data = response.json()

    for group in data['groups']:
        if group['name'] == group_name:
            return group['id']
    
    print('Failed to get group, expected "{}" found NONE.'.format(group_name))
    exit()

# -----------------------------------
group_id = get_group_id_by_name('Qlixar')

from_macros_endpoint = from_zendesk + '/api/v2/macros.json'

macro_count = 0

while from_macros_endpoint:
    response = requests.get(from_macros_endpoint, auth=from_credentials)

    if response.status_code != 200:
        print('Failed to retrieve articles with error {}'.format(response.status_code))
        exit()
    data = response.json()

    for macro in data['macros']:
        # Delete fields that will be automatically created 
        # del macro['url']
        # del macro['id']
        # del macro['updated_at']
        # del macro['created_at']

        restriction = {}
        restriction['type'] = 'Group'
        restriction['id'] = group_id
        restriction['ids'] = [group_id]
        macro['restriction'] = restriction


        # Create macro on the new account
        to_macros_endpoint = to_zendesk + '/api/v2/macros.json'
        response = requests.post(to_macros_endpoint, json={'macro': macro}, auth=to_credentials)
        
        if response.status_code == 201:
            macro_count += 1
            print('Macro created: "{}"'.format(macro["title"]))
        else:
            print('Failed to update article "{}" with error "{}", "{}"'.format(macro["title"], response.status_code, response.reason))
        
    from_macros_endpoint = data['next_page']

print(macro_count)
