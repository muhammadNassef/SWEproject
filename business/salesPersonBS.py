from business.baseBS import BaseBS
from dataAccess.salesPersonDA import SalesPersonDA


class SalesPersonBS(BaseBS):

    def findAll(self):
        return SalesPersonDA().findAll()

    def findById(self, id):
        return SalesPersonDA().findById(id)

    def save(self, salesPerson):
        return SalesPersonDA().save(salesPerson)

    def delete(self, id):
        return SalesPersonDA().delete(id)

    def update(self, id, data):
        return SalesPersonDA().update(id, data)
