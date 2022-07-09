from parsel import Selector
import time
import requests


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
        response.raise_for_status()
        return response.text
    except (requests.ReadTimeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_novidades(html_content):
    urls_list = []
    selector = Selector(html_content)
    for card in selector.css("h2.entry-title"):
        url = card.css("a::attr(href)").get()
        urls_list.append(url)
    return urls_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("span.current + a.page-numbers::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
