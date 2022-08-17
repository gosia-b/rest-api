import pandas as pd
from flask import Flask

from database import connect_to_db

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    conn = connect_to_db()
    query = 'SELECT * FROM users'
    df = pd.read_sql(query, conn)
    return df.to_json(orient='records')


if __name__ == '__main__':
    app.run()
