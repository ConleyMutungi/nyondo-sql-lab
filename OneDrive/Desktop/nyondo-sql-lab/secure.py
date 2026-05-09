import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

# TODO: rewrite using ? placeholder - never use f-strings in SQL
def search_product_safe(name):
    query = "SELECT * FROM products WHERE name LIKE ?"
    return conn.execute(query, (f'%{name}%',)).fetchall()

def login_safe(username, password):
    query = "SELECT * FROM users WHERE username=? AND password=?"
    return conn.execute(query, (username, password)).fetchone()

pass

# These must ALL return [] or None when you run them
print('Test 1:', search_product_safe("' OR 1=1--"))
print('Test 2:', search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print('Test 3:', login_safe("admin'--", 'anything'))
print('Test 4:', login_safe("' OR '1'='1", "' OR '1'='1"))