import psycopg2 as psy

# Establishing connection
connection = psy.connect(
    database="postgres",
    user="postgres",
    password="admin123",
    host="localhost",
    port="5432"
)
print("Database connected successfully")

# Creating a cursor object
cursor = connection.cursor()