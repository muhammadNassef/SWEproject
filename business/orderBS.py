from business.baseBS import BaseBS
from dataAccess.orderDA import OrderDA


class OrderBS(BaseBS):

    def findAll(self):
        return OrderDA().findAll()

    def findById(self, id):
        return OrderDA().findById(id)

    def save(self, order):
        return OrderDA().save(order)

    def delete(self, id):
        return OrderDA().delete(id)

    def update(self, id, data):
        pass
