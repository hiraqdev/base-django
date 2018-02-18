from abc import ABC, abstractmethod

class BaseService(ABC):

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def call(self):
        pass
