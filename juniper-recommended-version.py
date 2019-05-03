import requests
from bs4 import BeautifulSoup

url = 'https://kb.juniper.net/InfoCenter/index?page=content&id=KB21476'


def soupify_url_lxml():
    '''
    Given a URL returns BeautifulSoup object
    '''
    # URL where Juniper stores this information.
    result = requests.get(url)
    # Extract the content from the request
    content = result.content
    # Soupify the content
    soup = BeautifulSoup(content, 'lxml')

    return soup


soup = soupify_url_lxml()

entry_list = []

# Loop over the content
for entry in soup.find_all('tr'):
    entry_list.append(entry)

del entry_list[0]
del entry_list[0]
del entry_list[0]
del entry_list[0]
del entry_list[0]
del entry_list[0]
del entry_list[0]
del entry_list[0]
del entry_list[0]
del entry_list[0]
del entry_list[0]
del entry_list[0]
del entry_list[-1]

for entry in entry_list:
    print(entry)
