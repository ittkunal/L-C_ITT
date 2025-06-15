from apscheduler.schedulers.background import BackgroundScheduler
from server.services.news_fetcher import fetch_and_store_news

def scheduled_job():
    fetch_and_store_news()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_job, 'interval', hours=3)
    scheduler.start()