from business.baseBS import BaseBS
from dataAccess.customerDA import CustomerDA


class CustomerBS(BaseBS):

    def findAll(self):
        data = [('id', 'name', 'governrate', 'town', 'street_number', 'balance', 'salesperson_id')]
        for customer in CustomerDA().findAll():
            data.append(customer)
        return data

    def findById(self, id):
        return CustomerDA().findById(id)

    def delete(self, id):
        return CustomerDA().delete(id)

    def save(self, customer):
        return CustomerDA().save(customer)

    def update(self, id, data):
        return CustomerDA().update(id, data)
