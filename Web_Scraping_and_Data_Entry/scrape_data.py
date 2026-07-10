from pprint import pprint

from bs4 import BeautifulSoup
from config import google_form,zillow_clone
# from urllib3.util import url
import requests
class SCRAPE:

    def __init__(self,url):
        self.response = requests.get(url)
        # pprint(response.text)
        web = self.response.text
        self.soup = BeautifulSoup(web, 'html.parser')
        self.links = []
        self.prices = []
        self.addresses = []

    def get_lists(self):
        cards = self.soup.find_all("article", {"data-test": "property-card"})
        for card in cards:
            # Link
            link_tag = card.find("a", {"data-test": "property-card-link"})
            link = link_tag["href"] if link_tag else None

            # Price
            price_tag = card.find("span", {"data-test": "property-card-price"})
            price = price_tag.get_text(strip=True) if price_tag else None

            # Address
            address_tag = card.find("address", {"data-test": "property-card-addr"})
            address = address_tag.get_text(strip=True) if address_tag else None

            self.links.append(link)
            self.prices.append(price)
            self.addresses.append(address)
        return self.links,self.prices,self.addresses

# print(links)
# print(prices)
# print(addresses)