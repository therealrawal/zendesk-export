import os
import requests
from bs4 import BeautifulSoup

# Settings
zendesk = 'https://sliide.zendesk.com'
credentials = 'EMAIL', 'PASSWORD'
backup_folder = '2020-08-05'
language = 'en_us'
restore_list = [115001666554,115001663593,115001663573,115001666294,115001666274,115001663713,115001663633,115001666314,115001666234,115001666614,115001666494,115001666594,115001663653,115001663873,115001666354,115001666634,115001666334]

# Verify backup path is OK
backup_path = os.path.join(backup_folder, language)
if not os.path.exists(backup_path):
    print('The specified backup path does not exist. Check the folder name and locale.')
    exit()

# Restore articles
for article in restore_list:
    file_path = os.path.join(backup_path, str(article) + '.html')
    with open(file_path, mode='r', encoding='utf-8') as f:
        html_source = f.read()
    tree = BeautifulSoup(html_source, 'lxml')
    title = tree.h1.string.strip()
    tree.h1.decompose()

    payload = {'translation': {'title': title, 'body': str(tree.body)}}

    endpoint = '/api/v2/help_center/{loc}/articles/{id}/translations/.json'.format(id=article, loc=language.lower())
    url = zendesk + endpoint
    response = requests.post(url, json=payload, auth=credentials)
    if response.status_code == 200:
        print('Article {} restored'.format(article))
    else:
        print('Failed to update article {} with error {}, {}'.format(article, response.status_code, response.reason))