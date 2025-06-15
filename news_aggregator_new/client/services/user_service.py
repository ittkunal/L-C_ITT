import requests
from client.utils.session_store import get_session

API_URL = "http://localhost:8000"

def show_headlines_menu():
    session = get_session()
    user_id = session.get("user_id")
    print("\nHeadlines Menu:")
    print("1. Today")
    print("2. Date range")
    print("3. Logout")
    choice = input("Enter your choice: ")
    if choice == "1":
        resp = requests.get(f"{API_URL}/news/headlines")
        articles = resp.json()
        if not articles:
            print("No headlines found for today.")
        else:
            print("\nH E A D L I N E S")
            for art in articles:
                print(f"Article Id: {art['id']}")
                print(f"{art['title']}")
                if art.get('content'):
                    print(f"{art['content'][:100]}...")  # Show first 100 chars
                print(f"source: {art['source']}")
                print(f"URL: {art['url']}")
                print(f"Category: {art['category']}")
                print("-" * 40)
            print("1. Back")
            print("2. Logout")
            print("3. Save Article")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "3":
                article_id = input("Enter Article ID to save: ")
                resp = requests.post(f"{API_URL}/user/saved-articles", params={"user_id": user_id, "article_id": article_id})
                print(resp.json().get("message", "Failed to save."))
    elif choice == "2":
        start = input("Start date (YYYY-MM-DD): ")
        end = input("End date (YYYY-MM-DD): ")
        resp = requests.get(f"{API_URL}/news/headlines", params={"start": start, "end": end})
        articles = resp.json()
        if not articles:
            print("No headlines found for the selected date range.")
        else:
            print("\nH E A D L I N E S")
            for art in articles:
                print(f"Article Id: {art['id']}")
                print(f"{art['title']}")
                if art.get('content'):
                    print(f"{art['content'][:100]}...")
                print(f"source: {art['source']}")
                print(f"URL: {art['url']}")
                print(f"Category: {art['category']}")
                print("-" * 40)
            print("1. Back")
            print("2. Logout")
            print("3. Save Article")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "3":
                article_id = input("Enter Article ID to save: ")
                resp = requests.post(f"{API_URL}/user/saved-articles", params={"user_id": user_id, "article_id": article_id})
                print(resp.json().get("message", "Failed to save."))
    elif choice == "3":
        return

def show_saved_articles_menu():
    session = get_session()
    user_id = session.get("user_id")
    resp = requests.get(f"{API_URL}/user/saved-articles", params={"user_id": user_id})
    articles = resp.json()
    if not articles:
        print("No saved articles found.")
    else:
        print("\nS A V E D")
        for art in articles:
            print(f"Article Id: {art['id']} {art['title']}")
            if art.get('content'):
                print(f"{art['content'][:100]}...")
            print(f"source: {art['source']}")
            print(f"URL: {art['url']}")
            print(f"Category: {art['category']}")
            print("-" * 40)
    print("1. Delete Article")
    print("2. Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        article_id = input("Enter Article ID to delete: ")
        resp = requests.delete(f"{API_URL}/user/saved-articles/{article_id}", params={"user_id": user_id})
        print(resp.json().get("message", "Failed to delete."))

def search_articles():
    q = input("Enter search query: ")
    resp = requests.get(f"{API_URL}/news/search", params={"q": q})
    articles = resp.json()
    if not articles:
        print("No articles found for your search.")
    else:
        print("\nS E A R C H")
        for art in articles:
            print(f"Article Id: {art['id']} {art['title']}")
            if art.get('content'):
                print(f"{art['content'][:100]}...")
            print(f"source: {art['source']}")
            print(f"URL: {art['url']}")
            print(f"Category: {art['category']}")
            print("-" * 40)
    print("1. Save Article")
    print("2. Like Article")
    print("3. Dislike Article")
    print("4. Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        article_id = input("Enter Article ID to save: ")
        session = get_session()
        user_id = session.get("user_id")
        resp = requests.post(f"{API_URL}/user/saved-articles", params={"user_id": user_id, "article_id": article_id})
        print(resp.json().get("message", "Failed to save."))
    elif choice == "2":
        article_id = input("Enter Article ID to like: ")
        session = get_session()
        user_id = session.get("user_id")
        resp = requests.post(f"{API_URL}/news/{article_id}/like", params={"user_id": user_id})
        print(resp.json().get("message", "Failed to like."))
    elif choice == "3":
        article_id = input("Enter Article ID to dislike: ")
        session = get_session()
        user_id = session.get("user_id")
        resp = requests.post(f"{API_URL}/news/{article_id}/dislike", params={"user_id": user_id})
        print(resp.json().get("message", "Failed to dislike."))

def show_notifications_menu():
    session = get_session()
    user_id = session.get("user_id")
    resp = requests.get(f"{API_URL}/user/notifications", params={"user_id": user_id})
    notifications = resp.json()
    if not notifications:
        print("No notification settings found.")
    else:
        print("Your notification settings:")
        for n in notifications:
            print(f"Type: {n['type']}, Keywords: {n['keywords']}, Enabled: {n['enabled']}")
    print("1. Configure Notifications")
    print("2. Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        keywords = input("Enter keywords (comma separated): ")
        enabled = input("Enable notifications? (yes/no): ").lower() == "yes"
        resp = requests.put(f"{API_URL}/user/notifications", params={"user_id": user_id, "keywords": keywords, "enabled": enabled})
        print(resp.json().get("message", "Failed to update."))