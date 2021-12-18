import requests

zendesk = 'https://newsandrewards.zendesk.com/'
credentials = 'EMAIL', 'PASSWORD'

session = requests.Session()
session.auth = credentials

url = zendesk + 'api/v2/tickets.json?include=comment_count?per_page=1'

response = session.get(url)
if response.status_code != 200:
    print('Error with status code {}'.format(response.status_code))
    exit()

print(response.json())


