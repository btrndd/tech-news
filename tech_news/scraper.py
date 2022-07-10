# import calendar
# from datetime import datetime
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
    selector = Selector(html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("ul.post-meta > :nth-child(2)::text").get()

    writer = selector.css("span.author > a::text").get()

    # counting comments
    all_comments = selector.css("ol.comment-list > li.comment").getall()
    comments_count = 0
    if (all_comments is not None):
        comments_count = len(all_comments)
    # endregion

    summary_text_list = selector.css(
        "div.entry-content p:nth-child(2) *::text"
        ).getall()
    summary = ''.join(summary_text_list)

    tags = selector.css("a[rel=tag]::text").getall()
    category = selector.css("span.label::text").get()

    result = dict(zip(
        ["url", "title", "timestamp",
            "writer", "comments_count", "summary", "tags", "category"],
        [url, title, timestamp, writer,
            comments_count, summary, tags, category]
        ))
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
