import re
from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": re.compile(title, re.IGNORECASE)})
    news_result = []
    for news in news_list:
        news_result.append((news["title"], news["url"]))
    return news_result


# Requisito 7
def get_month_name(month):
    months = {
        "1": "janeiro",
        "2": "fevereiro",
        "3": "março",
        "4": "abril",
        "5": "maio",
        "6": "junho",
        "7": "julho",
        "8": "agosto",
        "9": "setembro",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro",
    }
    return months[month]


def search_by_date(date):
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d")
        month = get_month_name(str(formatted_date.month))
        text_date = f"{formatted_date.day} de {month} de {formatted_date.year}"
        news_list = search_news({"timestamp": text_date})

        news_result = []
        for news in news_list:
            news_result.append((news["title"], news["url"]))

        return news_result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news_list = search_news({"tags": re.compile(tag, re.IGNORECASE)})
    news_result = []
    for news in news_list:
        news_result.append((news["title"], news["url"]))
    return news_result


# Requisito 9
def search_by_category(category):
    news_list = search_news({"category": re.compile(category, re.IGNORECASE)})
    news_result = []
    for news in news_list:
        news_result.append((news["title"], news["url"]))
    return news_result
