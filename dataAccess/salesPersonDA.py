from dataAccess.baseDA import BaseDA
from dataAccess.connectionmanagment import ConnectionManagment
from entities.salesPerson import SalesPerson


class SalesPersonDA(BaseDA):

    def findAll(self):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        sql = 'select * from salesperson'
        cursor.execute(sql)
        data = cursor.fetchall()

        conn.commit()
        conn.close

        salespersonList = []
        for item in data:
            salesperson = SalesPerson(item[0], item[1], item[2], item[3], item[4], item[5])
            salespersonList.append(salesperson)

        return salespersonList

    def findById(self, id):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tupleId = (id,)
        sql = 'select * from salesperson where sp_id = %s'
        cursor.execute(sql, tupleId)

        item = cursor.fetchone()

        conn.commit()
        conn.close

        try:
            salesperson = SalesPerson(item[0], item[1], item[2], item[3], item[4], item[5])
        except:
            salesperson = SalesPerson(None, None, None, None, None, None)

        return salesperson

    def delete(self, id):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tupleId = (id,)
        sql = 'delete from salesperson where sp_id = %s'
        cursor.execute(sql, tupleId)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def save(self, salesPerson):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tuple_salesPerson = (salesPerson.id, salesPerson.name, salesPerson.governrate, salesPerson.town,
                             salesPerson.street_number, salesPerson.commission_rate)
        sql = 'insert into salesperson (sp_id,sp_name,governrate,town,street_number,commission_rate) ' \
              'values(%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, tuple_salesPerson)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False

    # salesPerson commission_rate update
    def update(self, id, data):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        sql = 'UPDATE salesperson SET commission_rate = %s where sp_id = %s'
        tuple_update = (data, id)
        cursor.execute(sql, tuple_update)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False
