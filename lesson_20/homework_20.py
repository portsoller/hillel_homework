import psycopg2
from faker import Faker

fake = Faker()
random_product = fake.word().capitalize()
random_category = fake.word().capitalize()
random_desc = fake.sentence(nb_words=4)
random_price = round(fake.pyfloat(min_value=10, max_value=1000), 2)

dbname = 'education_platform'
user = 'teacher'
password = 'super_password'
host = 'localhost'
port = '5432'

# Спроба підключитись до бази даних
try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database successfully!")

    # Для виконання запитів ви можете створити курсор
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
            	id SERIAL PRIMARY KEY,
            	name VARCHAR(50) NOT NULL,
            	description VARCHAR(100)
            );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    	id SERIAL PRIMARY KEY,
    	name VARCHAR(50) NOT NULL,
    	description VARCHAR(100) NOT NULL,
    	price NUMERIC(10, 2) NOT NULL,
    	category_id INT REFERENCES categories(id)
    );''')

    cursor.execute('''
        INSERT INTO categories (name, description) VALUES (%s, %s);''',
                   (random_category, random_desc));

    cursor.execute('''
        INSERT INTO products (name, description, price, category_id) VALUES (%s, %s, %s, %s);''',
                   (random_product, random_desc, random_price, 1));

    connection.commit()

    cursor.execute('''
    SELECT  products.name AS product_name, 
    products.description AS product_description, 
    price, 
    categories.name AS category_name
    FROM products 
    JOIN categories 
    ON products.category_id = categories.id;''')

    rows = cursor.fetchall()
    for row in rows:
        print(row)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # Закриваємо підключення
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
