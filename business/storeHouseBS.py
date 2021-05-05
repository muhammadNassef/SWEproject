from business.baseBS import BaseBS
from dataAccess.storeHouseDA import StoreHouseDA


class StoreHouseBS(BaseBS):

    def findAll(self):
        return StoreHouseDA().findAll()

    def findById(self, id):
        return StoreHouseDA().findById(id)

    def save(self, salesPerson):
        return StoreHouseDA().save(salesPerson)

    def delete(self, id):
        return StoreHouseDA().delete(id)

    def update(self, id, data):
        pass
