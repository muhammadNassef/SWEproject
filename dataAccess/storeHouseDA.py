from dataAccess.baseDA import BaseDA
from dataAccess.connectionmanagment import ConnectionManagment
from entities.storeHouse import StoreHouse


class StoreHouseDA(BaseDA):

    def findAll(self):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        sql = 'select * from storehouse'
        cursor.execute(sql)
        data = cursor.fetchall()

        conn.commit()
        conn.close

        storeHouseList = []
        for item in data:
            storeHouse = StoreHouse(item[0], item[1])
            storeHouseList.append(storeHouse)

        return storeHouseList

    def findById(self, id):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tuple_id = (id,)
        sql = 'select * from storehouse where store_number = %s'
        cursor.execute(sql, tuple_id)

        item = cursor.fetchone()

        conn.commit()
        conn.close

        try:
            storeHouse = StoreHouse(item[0], item[1])
        except:
            storeHouse = StoreHouse(None, None)

        return storeHouse

    def delete(self, id):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tupleId = (id,)
        sql = 'delete from storehouse where store_number = %s'
        cursor.execute(sql, tupleId)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def save(self, storeHouse):

        conn = ConnectionManagment.getConnection()

        cursor = conn.cursor()
        tuple_storeHouse = (storeHouse.number, storeHouse.place)
        sql = 'insert into storehouse (store_number,store_place) values(%s,%s)'
        cursor.execute(sql, tuple_storeHouse)

        conn.commit()
        conn.close

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def update(self):
        pass
