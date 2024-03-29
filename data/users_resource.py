from flask import jsonify
from flask_restful import abort, Resource, reqparse

from data import db_session
from data.users import User
parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)
parser.add_argument('hashed_password', required=True)
parser.add_argument('modified_date', required=True)


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"Users {users_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        return jsonify({'users': users.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality',
                  'address', 'email', 'hashed_password', 'modified_date'))})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
               only=('surname', 'name', 'age', 'position', 'speciality',
                     'address', 'email', 'hashed_password', 'modified_date')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
             surname=args['surname'],
             name=args['name'],
             age=args['age'],
             position=args['position'],
             speciality=args['speciality'],
             address=args['address'],
             email=args['email'],
             hashed_password=args['hashed_password'],
             modified_date=args['modified_date']
        )
        session.add(users)
        session.commit()
        return jsonify({'id': users.id})