import os
import psycopg2
import pytest
from faker import Faker

fake = Faker()

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'education_platform')
DB_USER = os.getenv('DB_USER', 'teacher')
DB_PASS = os.getenv('DB_PASSWORD', 'super_password')
DB_PORT = os.getenv('DB_PORT', '5432')


@pytest.fixture(scope="module")
def db_connection():
    # Спроба підключитись до бази даних
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    # Для виконання запитів ви можете створити курсор
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            description VARCHAR(100)
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            description VARCHAR(100) NOT NULL,
            price NUMERIC(10, 2) NOT NULL,
            category_id INT REFERENCES categories(id) ON DELETE CASCADE
        );
    ''')
    connection.commit()
    cursor.close()

    yield connection

    # Закриваємо підключення
    connection.close()

def test_connection(db_connection):
    assert db_connection is not None
    assert db_connection.status == psycopg2.extensions.STATUS_READY

def test_crud_operations(db_connection):
    cursor = db_connection.cursor()

    cat_name = fake.word().capitalize()
    prod_name = fake.word().capitalize()
    new_price = 150.50

    cursor.execute("INSERT INTO categories (name) VALUES (%s) RETURNING id;", (cat_name,))
    category_id = cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO products (name, description, price, category_id) VALUES (%s, %s, %s, %s) RETURNING id;",
        (prod_name, "Test description", 99.99, category_id)
    )
    product_id = cursor.fetchone()[0]
    db_connection.commit()

    cursor.execute("SELECT name, price FROM products WHERE id = %s;", (product_id,))
    product = cursor.fetchone()
    assert product is not None
    assert product[0] == prod_name
    assert float(product[1]) == 99.99

    cursor.execute("UPDATE products SET price = %s WHERE id = %s;", (new_price, product_id))
    db_connection.commit()

    cursor.execute("SELECT price FROM products WHERE id = %s;", (product_id,))
    updated_price = cursor.fetchone()[0]
    assert float(updated_price) == new_price

    cursor.execute("DELETE FROM products WHERE id = %s;", (product_id,))
    db_connection.commit()

    cursor.execute("SELECT * FROM products WHERE id = %s;", (product_id,))
    deleted_product = cursor.fetchone()
    assert deleted_product is None

    cursor.close()
