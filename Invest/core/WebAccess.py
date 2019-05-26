from urllib.request import urlopen as urlopen
from bs4 import BeautifulSoup as Soup


def parse_website(website):
    client = urlopen(website)
    client_read = client.read()
    client.close()
    client_soup = Soup(client_read, "html.parser")
    return client_soup
