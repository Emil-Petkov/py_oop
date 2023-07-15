from abc import ABC, abstractmethod


class DatabaseInterface(ABC):

    @abstractmethod
    def save(self, data):
        pass


class Database(DatabaseInterface):
    def save(self, data):
        pass


class Application:
    def __init__(self, database):
        self.database = database

    def run(self):
        data = self.fetch_data()
        self.database.save(data)

    def fetch_data(self):
        pass


################################################################

# Dependency injection

class MessageService:
    def send_message(self):
        pass


class Email(MessageService):
    def send_message(self):
        pass


class Notification:
    def __init__(self, service: MessageService):
        self._service = service

    def promotional_notification(self):
        self._service.send_message()
