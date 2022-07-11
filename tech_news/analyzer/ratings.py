from collections import Counter
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
    news_list = find_news()
    categories_list = map(
            lambda row: row["category"],
            news_list
        )

    categories_count_dict = Counter(categories_list).items()
    sorted_categories = sorted(
        categories_count_dict, key=lambda row: row[1], reverse=1)

    result = []
    for category in sorted_categories:
        result.append(category[0])
    return result[:5]
