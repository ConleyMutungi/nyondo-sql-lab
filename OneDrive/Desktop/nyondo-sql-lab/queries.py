import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

# Query A - Get every column of every product
rows = conn.execute("SELECT * FROM products").fetchall()
print("Query A:", rows)

# Query B - Get only the name and price of all products
rows = conn.execute("SELECT name, price FROM products").fetchall()
print("Query B:", rows)

# Query C - Get full details of the product with id = 3
rows = conn.execute("SELECT * FROM products WHERE id = 3").fetchall()
print("Query C:", rows)

# Query D - Find all products whose name contains 'sheet'
rows = conn.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall()
print("Query D:", rows)

# Query E - Get all products sorted by price, highest first
rows = conn.execute("SELECT * FROM products ORDER BY price DESC").fetchall()
print("Query E:", rows)

# Query F - Get only the 2 most expensive products
rows = conn.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2").fetchall()
print("Query F:", rows)

# Query G - Update the price of Cement (id=1) to 38,000 then SELECT * to confirm
conn.execute("UPDATE products SET price = 38000 WHERE id = 1")
conn.commit()
rows = conn.execute("SELECT * FROM products").fetchall()
print("Query G:", rows)