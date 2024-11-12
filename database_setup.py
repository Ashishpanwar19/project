import sqlite3
import json

# Load JSON data
with open("C://Users//ashis//Downloads//jsondata.json", encoding='utf-8') as f:
    data = json.load(f)

# Connect to SQLite database
conn = sqlite3.connect('dashboard.db')
cursor = conn.cursor()

# Create table with relevant columns (adjust columns based on your JSON structure)
cursor.execute('''
CREATE TABLE IF NOT EXISTS dashboard_data (
    id INTEGER PRIMARY KEY,
    intensity INTEGER,
    likelihood INTEGER,
    relevance INTEGER,
    year INTEGER,
    country TEXT,
    topic TEXT,
    region TEXT,
    city TEXT
)
''')

# Insert data into table
for entry in data:
    cursor.execute('''
    INSERT INTO dashboard_data (intensity, likelihood, relevance, year, country, topic, region, city)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        entry.get('intensity'),
        entry.get('likelihood'),
        entry.get('relevance'),
        entry.get('year'),
        entry.get('country'),
        entry.get('topic'),
        entry.get('region'),
        entry.get('city')
    ))

conn.commit()
conn.close()
print("Data loaded into SQL database successfully.")
