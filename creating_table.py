from connect import connection, cursor

# Creating a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        code SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price NUMERIC(10, 2) NOT NULL
    )
''')

if __name__ == "__main__":
    connection.commit()
    connection.close()