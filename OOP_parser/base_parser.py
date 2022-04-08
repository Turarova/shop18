from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

class BaseParser:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        # self.proxy = None
        # self.soup = BeautifulSoup
        self.headers = {}


    def _set_proxy(self):
        pass

    def set_user_agent(self):
        ua = UserAgent()
        self.headers['User-Agent'] = ua.random

    def get(self, url):
        self.set_user_agent()
        response = requests.get(url, headers = self.headers)
        return response.text

    def init_soup(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    # полиморфные методы:
    def get_links_data(self):
        raise NotImplementedError
    
    def get_details_data(self):
        raise NotImplementedError