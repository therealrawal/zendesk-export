import requests

# Set the request parameters
url = 'https://newsandrewards.zendesk.com//api/v2/help_center/en-us/articles.json'
user = 'EMAIL'
pwd = 'PASSWORD'

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
print(response.json())


