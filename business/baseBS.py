from abc import ABCMeta, abstractmethod


class BaseBS(metaclass=ABCMeta):
    @abstractmethod
    def findAll(self):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def save(self, obj):
        pass

    @abstractmethod
    def update(self, id, data):
        pass
