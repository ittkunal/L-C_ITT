import requests
from server.config import Config
from server.services.categorizer import categorize_article
from server.repositories.article_repo import store_articles

def fetch_news_from_newsapi():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={Config.NEWSAPI_KEY}"
    response = requests.get(url)
    return response.json().get("articles", [])

def fetch_news_from_thenewsapi():
    url = f"https://api.thenewsapi.com/v1/news/top?api_token={Config.THENEWSAPI_KEY}&locale=us"
    response = requests.get(url)
    return response.json().get("data", [])

def fetch_and_store_news():
    articles = []
    for fetcher in [fetch_news_from_newsapi, fetch_news_from_thenewsapi]:
        for item in fetcher():
            category = item.get("category") or categorize_article(item.get("title", "") + " " + item.get("description", ""))
            articles.append({
                "title": item.get("title"),
                "content": item.get("description"),
                "url": item.get("url"),
                "source": item.get("source", {}).get("name", "Unknown") if isinstance(item.get("source"), dict) else item.get("source", "Unknown"),
                "category": category,
                "published_at": item.get("publishedAt")
            })
    store_articles(articles)