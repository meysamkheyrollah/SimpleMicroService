# myapp/tasks.py
from celery import shared_task
from abc import abstractmethod, ABC
from enum import Enum


class OTPType(Enum):
    TransactionOTP = 'TransactionOTP'
    LoginOTP = 'LoginOTP'

class BackendType(Enum):
    Email = 'Email'
    SMS = 'SMS'
    Telegram = 'Telegram'


@shared_task
def MessageWorker(code):
    type = OTPType.TransactionOTP.value
    print(type) 
    print( type + f' sent with code which is {code}')




class ProviderInterface(ABC):
    type: BackendType

    @classmethod
    @abstractmethod
    def verify(cls): ...

    @classmethod
    @abstractmethod
    def send(cls, code): ...

    @classmethod
    def execute(cls, code):
        cls.verify()
        cls.send(code)


class MobileInterface(ProviderInterface):
    type: BackendType = BackendType.SMS

    @classmethod
    def verify(cls):...

    @classmethod
    def send(cls, code): 
        print('inside interface', code)
        MessageWorker.delay(code)


class EmailInterface(ProviderInterface):
    provider_name: BackendType.Email

    @classmethod
    def verify(cls): ...

    @classmethod
    def send(cls, code):
        MessageWorker.delay(code)


class TelegramInterface(ProviderInterface):
    provider_name: BackendType.Telegram

    @classmethod
    def verify(cls): ...

    @classmethod
    def send(cls, code):
        MessageWorker.delay(code)
