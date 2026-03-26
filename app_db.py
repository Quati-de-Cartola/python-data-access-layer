from psycopg2 import Error
from faker import Faker
from connect import connection, cursor

class AppDB:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect_to_db()
    
    def connect_to_db(self):
        self.conn = connection
        self.cur = cursor
        print("Connection with Database established successfully")

    def select_data(self):
        try:
            self.cur.execute("SELECT * FROM product ORDER BY code")
            products = self.cur.fetchall()
            return products
        except (Exception, Error) as e:
            print(f"Error fetching data: {e}")
            return []
        
    def insert_data(self, name, price):
        try:
            self.cur.execute('''
                INSERT INTO product (name, price) VALUES (%s, %s)
            ''', (name, price))
            self.conn.commit()
            print(f"Product '{name}' inserted successfully with price {price}")
        except (Exception, Error) as e:
            print(f"Error inserting data: {e}")

    def delete_data(self, code):
        try:
            self.cur.execute('''DELETE FROM product WHERE code = %s''', (code,))
            self.conn.commit()
            print(f"Product with code '{code}' deleted successfully")
        except (Exception, Error) as e:
            print(f"Error deleting data: {e}")

    def update_data(self, code, name, price):
        try:
            self.cur.execute('''
                UPDATE product SET name = %s, price = %s WHERE code = %s
            ''', (name, price, code))
            self.conn.commit()
            print(f"Product with code '{code}' updated successfully to name '{name}' and price {price}")
        except (Exception, Error) as e:
            print(f"Error updating data: {e}")
    
    def get_all_products(self):
        return self.select_data()

if __name__ == "__main__":
    app_db = AppDB()
    fake = Faker()

    for _ in range(10):
        name = fake.word()
        price = round(fake.random_number(digits=5) / 100, 2)
        app_db.insert_data(name, price)