from flask import Flask, jsonify, request

from database import connect_to_db, create_db_table

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = 'SELECT * FROM users'
    cursor.execute(query)
    return jsonify(cursor.fetchall())


@app.route('/users', methods=['POST'])
def insert_user():
    user = request.get_json()
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'INSERT INTO users(name, email, address, phone) VALUES (?, ?, ?, ?)'
    cursor.execute(statement, (user['name'], user['email'], user['address'], user['phone']))
    conn.commit()
    return jsonify(True)


if __name__ == '__main__':
    create_db_table()
    app.run()
