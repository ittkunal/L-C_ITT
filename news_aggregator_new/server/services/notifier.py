from server.repositories.notification_repo import get_users_for_notification
from server.services.mailer import send_email

def send_batch_notifications():
    users = get_users_for_notification()
    for user in users:
        # Compose email body with relevant articles (implement as needed)
        body = "Here are your news notifications..."
        send_email(user["email"], "Your News Digest", body)