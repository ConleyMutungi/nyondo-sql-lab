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

import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

# --- Validation helpers ---
def validate_name(name):
    if not isinstance(name, str):
        print("Error: name must be a string")
        return False
    if len(name) < 2:
        print("Error: name must be at least 2 characters")
        return False
    if any(c in name for c in "<>;"):
        print("Error: name contains invalid characters")
        return False
    return True

def validate_price(price):
    try:
        price = float(price)
        if price <= 0:
            print("Error: price must be positive")
            return False
    except ValueError:
        print("Error: price must be a number")
        return False
    return True

def validate_username(username):
    if not isinstance(username, str):
        print("Error: username must be a string")
        return False
    if not username.strip():
        print("Error: username cannot be empty")
        return False
    if " " in username:
        print("Error: username cannot contain spaces")
        return False
    return True

def validate_password(password):
    if not isinstance(password, str):
        print("Error: password must be a string")
        return False
    if len(password) < 6:
        print("Error: password must be at least 6 characters")
        return False
    return True

# --- Secure functions with validation ---
def search_product_safe(name):
    if not validate_name(name):
        return None
    query = "SELECT * FROM products WHERE name LIKE ?"
    rows = conn.execute(query, (f"%{name}%",)).fetchall()
    return rows

def login_safe(username, password):
    if not validate_username(username) or not validate_password(password):
        return None
    query = "SELECT * FROM users WHERE username=? AND password=?"
    row = conn.execute(query, (username, password)).fetchone()
    return row

# --- Tests ---
print("Test 1:", search_product_safe("cement"))       # works
print("Test 2:", search_product_safe(""))             # rejected
print("Test 3:", search_product_safe("<script>"))     # rejected
print("Test 4:", login_safe("admin", "admin123"))     # works
print("Test 5:", login_safe("admin", "ab"))           # rejected (too short)
print("Test 6:", login_safe("ad min", "pass123"))     # rejected (space in username)