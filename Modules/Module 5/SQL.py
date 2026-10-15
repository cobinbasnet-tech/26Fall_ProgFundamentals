import sqlite3

conn = sqlite3.connect("school.db") 
cur = conn.cursor()

conn.close()
print("\nDone.")