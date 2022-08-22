import flask.wrappers
from flask import Flask, jsonify, request

from database import connect_to_db, create_db_table

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users() -> flask.wrappers.Response:
    conn = connect_to_db()
    cursor = conn.cursor()
    query = 'SELECT * FROM users'
    cursor.execute(query)
    return jsonify(cursor.fetchall())


@app.route('/users', methods=['POST'])
def insert_user() -> flask.wrappers.Response:
    user = request.get_json()
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'INSERT INTO users(name, email, address, phone) VALUES (?, ?, ?, ?)'
    cursor.execute(statement, (user['name'], user['email'], user['address'], user['phone']))
    conn.commit()
    return jsonify(True)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id: int) -> flask.wrappers.Response:
    conn = connect_to_db()
    cursor = conn.cursor()
    query = 'SELECT * FROM users WHERE user_id = ?'
    cursor.execute(query, user_id)
    return jsonify(cursor.fetchall())


@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id: int) -> flask.wrappers.Response:
    user = request.get_json()
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'UPDATE users SET name = ?, email = ?, address = ?, phone = ? WHERE user_id = ?'
    cursor.execute(statement, (user['name'], user['email'], user['address'], user['phone'], user_id))
    conn.commit()
    return jsonify(True)


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id: int) -> flask.wrappers.Response:
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'DELETE FROM users WHERE user_id = ?'
    cursor.execute(statement, user_id)
    conn.commit()
    return jsonify(True)


if __name__ == '__main__':
    create_db_table()
    app.run()
