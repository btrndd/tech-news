import re
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": re.compile(title, re.IGNORECASE)})
    news_result = []
    for news in news_list:
        news_result.append((news["title"], news["url"]))
    return news_result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
