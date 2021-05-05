from business.baseBS import BaseBS
from dataAccess.productDA import ProductDA


class ProductBS(BaseBS):

    def findAll(self):
        return ProductDA().findAll()

    def findById(self, id):
        return ProductDA().findById(id)

    def save(self, product):
        return ProductDA().save(product)

    def delete(self, id):
        return ProductDA().delete(id)

    def update(self, id, data):
        return ProductDA().update(id, data)
