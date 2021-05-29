from dataAccess.baseDA import BaseDA
from dataAccess.connectionmanagment import ConnectionManagment
from entities.product import Product


class ProductDA(BaseDA):

    def findAll(self):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        sql = 'select * from product'
        cursor.execute(sql)
        data = cursor.fetchall()

        conn.commit()
        conn.close

        productList = []
        for item in data:
            product = Product(item[0], item[1], item[2], item[3])
            productList.append(product)

        return productList

    def findById(self, id):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tupleId = (id,)
        sql = 'select * from product where product_id = %s'
        cursor.execute(sql, tupleId)

        item = cursor.fetchone()

        conn.commit()
        conn.close

        try:
            product = Product(item[0], item[1], item[2], item[3])
        except:
            product = Product(None, None, None, None)

        return product

    def delete(self, id):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tupleId = (id,)
        sql = 'delete from product where product_id = %s'
        cursor.execute(sql, tupleId)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def save(self, product):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tuple_product = (product.id, product.desc, product.product_class, product.price)
        sql = 'insert into product (product_id,product_desc,product_class,price) values(%s,%s,%s)'
        cursor.execute(sql, tuple_product)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False

    # product price update
    def update(self, id, data):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        sql = 'UPDATE product SET price = %s where product_id = %s'
        tuple_update = (data, id)
        cursor.execute(sql, tuple_update)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False
