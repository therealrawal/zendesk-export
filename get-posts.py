import requests

zendesk = 'https://newsandrewards.zendesk.com/'
credentials = 'EMAIL', 'PASSWORD'

session = requests.Session()
session.auth = credentials

url = zendesk + '/api/v2/community/topics/'

response = session.get(url)
if response.status_code != 200:
    print('Error with status code {}'.format(response.status_code))
    exit()
print(response.json())





# topic_id = 114094824213
# url = zendesk + '/api/v2/community/topics/' + str(topic_id) + '/posts.json'
# response = session.get(url)
# if response.status_code != 200:
#     print('Error with status code {}'.format(response.status_code))
#     exit()
# data = response.json()
# topic_posts = data['posts']

# for post in topic_posts:
#     print(post['title'])