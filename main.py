from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


users = {
    '0': {
        'name': 'Colleen',
        'surname': 'Brown',
        'email': 'colleen.brown@example.com',
        'address': '3904 First Street',
        'phone': '(908) 256-2784'
    },
    '1': {
        'name': 'Christian',
        'surname': 'Fletcher',
        'email': 'christian.fletcher@example.com',
        'address': '7494 James St',
        'phone': '(563) 518-9948'
    },
    '2': {
        'name': 'Jon',
        'surname': 'Elliott',
        'email': 'jon.elliott@example.com',
        'address': '8067 Stevens Creek Blvd',
        'phone': '(551) 760-2152'
    },
    '3': {
        'name': 'Joy',
        'surname': 'Morris',
        'email': 'joy.morris@example.com',
        'address': '9018 W Sherman Dr',
        'phone': '(701) 539-7575'
    },
}


class User(Resource):
    def get(self, user_id):
        return users[user_id]


api.add_resource(User, '/user/<user_id>')

if __name__ == '__main__':
    app.run()
