from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_list = find_news()
    ordered_by_comments = sorted(
        news_list, key=lambda row: row['comments_count'], reverse=1)
    result = []
    for news in ordered_by_comments:
        result.append((news["title"], news["url"]))
    return result[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
