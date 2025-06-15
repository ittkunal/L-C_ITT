from server.db.db import get_db_connection
from datetime import datetime

def store_articles(articles):
    conn = get_db_connection()
    cursor = conn.cursor()
    for art in articles:
        cursor.execute("SELECT id FROM articles WHERE url=%s", (art["url"],))
        if not cursor.fetchone():
            cursor.execute(
                "INSERT INTO articles (title, content, url, source, category, published_at) VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    art["title"],
                    art["content"],
                    art["url"],
                    art["source"],
                    art["category"],
                    datetime.fromisoformat(art["published_at"].replace("Z", "+00:00"))
                )
            )
    conn.commit()
    cursor.close()
    conn.close()

def get_articles(date=None, start=None, end=None, category=None):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM articles WHERE 1=1"
    params = []
    if category:
        query += " AND category=%s"
        params.append(category)
    if date:
        query += " AND DATE(published_at)=%s"
        params.append(date)
    if start and end:
        query += " AND DATE(published_at) BETWEEN %s AND %s"
        params.extend([start, end])
    query += " ORDER BY published_at DESC"
    cursor.execute(query, tuple(params))
    articles = cursor.fetchall()
    cursor.close()
    conn.close()
    return articles

def get_article_by_id(article_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM articles WHERE id=%s", (article_id,))
    article = cursor.fetchone()
    cursor.close()
    conn.close()
    return article

def search_articles_db(q, start=None, end=None, sort_by=None):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT a.*, COALESCE(SUM(ld.like_dislike),0) as score FROM articles a LEFT JOIN likes_dislikes ld ON a.id=ld.article_id WHERE (a.title LIKE %s OR a.content LIKE %s)"
    params = [f"%{q}%", f"%{q}%"]
    if start and end:
        query += " AND DATE(a.published_at) BETWEEN %s AND %s"
        params.extend([start, end])
    query += " GROUP BY a.id"
    if sort_by == "likes":
        query += " ORDER BY score DESC"
    elif sort_by == "dislikes":
        query += " ORDER BY score ASC"
    else:
        query += " ORDER BY a.published_at DESC"
    cursor.execute(query, tuple(params))
    articles = cursor.fetchall()
    cursor.close()
    conn.close()
    return articles

def get_categories_db():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    cursor.close()
    conn.close()
    return categories

def like_article_db(article_id, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("REPLACE INTO likes_dislikes (user_id, article_id, like_dislike) VALUES (%s, %s, 1)", (user_id, article_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Article liked."}

def dislike_article_db(article_id, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("REPLACE INTO likes_dislikes (user_id, article_id, like_dislike) VALUES (%s, %s, -1)", (user_id, article_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Article disliked."}