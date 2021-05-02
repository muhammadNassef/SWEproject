from dataAccess.baseDA import BaseDA
from dataAccess.connectionmanagment import ConnectionManagment
from entities.order import Order


class OrderDA(BaseDA):

    def findAll(self):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        sql = 'select * from orders'
        cursor.execute(sql)
        data = cursor.fetchall()

        conn.commit()
        conn.close

        orderList = []
        for item in data:
            product = Order(item[0], item[1], item[2])
            orderList.append(product)

        return orderList

    def findById(self, id):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tuple_id = (id,)
        sql = 'select * from orders where order_id = %s'
        cursor.execute(sql, tuple_id)

        item = cursor.fetchone()

        conn.commit()
        conn.close

        try:
            order = Order(item[0], item[1], item[2])
        except:
            order = Order(None, None, None)

        return order

    def delete(self, id):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tupleId = (id,)
        sql = 'delete from orders where order_id = %s'
        cursor.execute(sql, tupleId)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def save(self, order):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tuple_order = (order.id, order.date, order.customer_id)
        sql = 'insert into orders (order_id,order_date,customer_id) values(%s,%s,%s)'
        cursor.execute(sql, tuple_order)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def update(self, id, data):
        pass
