from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Endpoint to fetch all data or filtered data
@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('dashboard.db')
    cursor = conn.cursor()

    # Query all data
    cursor.execute("SELECT * FROM dashboard_data")
    rows = cursor.fetchall()

    # Map results to JSON-like format
    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "intensity": row[1],
            "likelihood": row[2],
            "relevance": row[3],
            "year": row[4],
            "country": row[5],
            "topic": row[6],
            "region": row[7],
            "city": row[8]
        })

    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
