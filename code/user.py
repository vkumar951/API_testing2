import sqlite3
from flask_restful import Resource,reqparse



class User:
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password

    @classmethod    # we are using the authentication from the input as a username and then as per DB  , we would match it.
    def find_by_username(cls,username):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        query="SELECT * from USERS where username = ?"
        result=cursor.execute(query,(username,))  # parameters always ahve to be  tuple form
        row=result.fetchone() # fetching only first non null .
        if row:
            user=cls(*row)
        else:
            user=None

        connection.close()
        return user

    @classmethod    # we are using the authentication from the input as a ID and then as per DB  , we would match it.
    def find_by_id(cls,_id):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()

        query="SELECT * from USERS where id = ?"
        result=cursor.execute(query,(_id,))  # parameters always ahve to be  tuple form
        row=result.fetchone() # fetching only first non null .
        if row:
            user=cls(*row)
        else:
            user=None

        connection.close()
        return user


class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="The field cannot be blank")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="The field cannot be blank")

    def post(self):
        data=UserRegister.parser.parse_args()
        # adding the functionality to  not enter the same Username in the DB
        if User.find_by_username(data['username']):
            return {"message":"A user with that name already exists"},400

        connection=sqlite3.connect("data.db")
        cursor=connection.cursor()
        query="INSERT INTO USERS VALUES (NULL,?,?)"
        cursor.execute(query,(data['username'],data['password']))

        connection.commit()
        connection.close()
        return {"message":"User Created Successfully"},201


