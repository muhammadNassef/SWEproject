from dataAccess.connectionmanagment import ConnectionManagment
from entities.customer import Customer
from dataAccess.baseDA import BaseDA


class CustomerDA(BaseDA):

    def findAll(self):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        sql = 'select * from customer'
        cursor.execute(sql)
        data = cursor.fetchall()

        conn.commit()
        conn.close

        customerList = []
        for item in data:
            customer = Customer(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            customerList.append(customer)

        return customerList

    def findById(self, id):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tupleId = (id,)
        sql = 'select * from customer where customer_id = %s'
        cursor.execute(sql, tupleId)

        item = cursor.fetchone()

        conn.commit()
        conn.close

        try:
            customer = Customer(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
        except:
            customer = Customer(None, None, None, None, None, None, None)

        return customer

    def delete(self, id):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tupleId = (id,)
        sql = 'delete from customer where customer_id = %s'
        cursor.execute(sql, tupleId)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def save(self, customer):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tuple_customer = (customer.id, customer.name, customer.governrate, customer.town,
                          customer.street_number, customer.balance, customer.salesperson_id)
        sql = 'insert into customer (customer_id,customer_name,governrate,town,street_number,balance,sp_id)' \
              'values(%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, tuple_customer)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False

    # customer balance update
    def update(self, id, data):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        sql = 'UPDATE customer SET balance = %s where customer_id = %s'
        tuple_update = (data, id)
        cursor.execute(sql, tuple_update)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False
