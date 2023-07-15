from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotifier(Notifier):
    def send_notification(self, message):
        return f"Email Notification: {message}"


class SMSNotifier(Notifier):
    def send_notification(self, message):
        return f"SMS Notification: {message}"


def send_notifications(notifiers, message):
    for notifier in notifiers:
        print(notifier.send_notification(message))


notifications = [EmailNotifier(), SMSNotifier()]
send_notifications(notifications, "Hello, Open-Closed Principle!")

# Email Notification: Hello, Open-Closed Principle!
# SMS Notification: Hello, Open-Closed Principle!
