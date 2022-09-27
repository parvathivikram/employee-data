import psycopg2
import logging

class DataAccessObject:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = psycopg2.connect(host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port)

    def __enter__(self):
        logging.info("Calling __enter__")
        return self.connection.cursor()

    def __exit__(self, error: Exception, value: object, traceback: object):
        logging.info("Calling __exit__")
        self.connection.commit()
        self.connection.close()


"""
class DataAccessObject:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
    def establish_db_connection(self):
        conn = ""
        cursor = ""
        try:
            conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            cursor = conn.cursor()
        except Exception as err:
            print("Exception occurred", err)
        return [cursor, conn]
    def closing_connection(self):
        cursor, conn = self.establish_db_connection()
        cursor.close()
        conn.close()
    def table_creation(self):
        cursor, conn = self.establish_db_connection()
        query = "CREATE TABLE employee(FirstName VARCHAR(100), LastName VARCHAR(100), Eid INTEGER, UserId VARCHAR(100), Password VARCHAR(50), MobileNo VARCHAR(12), EmailId VARCHAR(50), DOB VARCHAR(50), Address VARCHAR(50), Gender VARCHAR(10), DOJ VARCHAR(50), Technology VARCHAR(50))"
        cursor.execute(query)
        conn.commit()
        self.closing_connection()
        return "Table is created"
    def data_insertion(self):
        cursor, conn = self.establish_db_connection()
        records = self.data_frm_service
        query = "INSERT INTO employee_information values(%s, %s, %s, %s)"
        count = 0
        for record in records:
            cursor.execute(query, record)
            count += 1
            print("query executed")
        print("Query executed", count)
        conn.commit()
        print("Table entries inserted")
        self.closing_connection()
"""



def db_ucheck(a1,a2):
    # Db Connection
    with DataAccessObject("localhost", "postgres", "postgres", "12345678", 5432) as cursor:
        # cursor ojbect
        # select query
        cursor.execute("SELECT * FROM employee WHERE eid={} AND userid={}".format(a1, a2))
        data = cursor.fetchone()
        if data == None:
            return False
        return True

def db_insert(*args):
    firstname, lastname, eid, userid, password, mobileno, emailid, dob, address, gender, doj, technology = args
    record = (firstname, lastname, eid, userid, password, mobileno, emailid, dob, address, gender, doj, technology)
    query = "INSERT INTO employee values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    with DataAccessObject("localhost", "postgres", "postgres", "12345678", 5432) as cursor:
        # cursor.execute(f"INSERT INTO employee(firstname, lastname, eid, userid, password, mobileno, emailid, dob, address, gender, doj, technology) values({firstname}, {lastname}, {eid}, {userid}, {password}, {mobileno}, {emailid}, {dob}, {address}, {gender}, {doj}, {technology})")
        cursor.execute(query, record)
    
    return {"message":f"{firstname} {lastname} user created successfully."}
    
def user_credentials(u_id, u_password):
    with DataAccessObject("localhost", "postgres", "postgres", "12345678", 5432) as cursor:
        cursor.execute("SELECT * FROM employee where eid={} AND password='{}'".format(u_id, u_password))
        data = cursor.fetchone()
    if data == None:
        return False
    return True

def update_password(u_id, u_password):
    with DataAccessObject("localhost", "postgres", "postgres", "12345678", 5432) as cursor:
        cursor.execute(f"UPDATE employee SET password = '{u_password}' WHERE eid = {u_id};")
    return {"message": "user password update successfully"}

def delete_user(e_id):
    with DataAccessObject("localhost", "postgres", "postgres", "12345678", 5432) as cursor:
        cursor.execute(f"DELETE FROM employee WHERE eid={e_id};")
    return {"message":"user delete successfully."}
    


if __name__ == "__main__":
    db_ucheck(1, 2)
    