from flask import Flask, jsonify, render_template, request
import MySQLdb

app = Flask(__name__)

# MySQL Configuration (Update with your credentials)
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="Nitu@123",  # Replace with your actual password
    db="mydatabase",
    charset="utf8",  # Ensure proper encoding
    use_unicode=True
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')  # Renders the Chart.js page

@app.route("/data")
def get_data():
    sector = request.args.get("sector")  # Get sector from URL query parameters

    query = "SELECT column1, column2, column3 FROM jsondata"
    params = ()

    if sector:  # Apply filtering if a sector is selected
        query += " WHERE sector = %s"
        params = (sector,)

    cursor.execute(query, params)
    data = cursor.fetchall()

    json_data = [{"column1": row[0], "column2": row[1], "column3": row[2]} for row in data]
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
