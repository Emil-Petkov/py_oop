from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyMLContent(IContent):
    def format(self):
        return f"<myML>\n" + self.text + "\n" + "</myML>\n"


class EncryptedContent(IContent):
    def format(self):
        result = ""

        for letter in self.text:
            result += chr(ord(letter) + 5)

        return result


class MaskedContent(IContent):
    def format(self):
        return "*" * len(self.text)


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol, content_type):
        self.protocol = protocol
        self.content_type = content_type
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join([receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content.format())


email = Email('IM', 'MyML')
email.set_sender('Ivan')
email.set_receiver('Emil')

email.set_content(MyMLContent('Hello, there!'))
# Sender: I'm Ivan
# Receiver: Emil
# Content:
# <myML>
# Hello, there!
# </myML>

email2 = Email('IM', 'MyML')
email2.set_sender('Emil')
email2.set_receiver('Nadezhda')

email2.set_content(EncryptedContent('Hello, there!'))
# Sender: I'm Emil
# Receiver: Nadezhda
# Content:
# Mjqqt1%ymjwj&

email3 = Email('IM', 'MyML')
email3.set_sender('Nadezhda')
email3.set_receiver('Ivan')

email3.set_content(MaskedContent('Hello, there!'))
# Sender: I'm Nadezhda
# Receiver: Ivan
# Content:
# *************

print(email)
print(f"{email2}\n")
print(email3)
