from flask import Flask
from flask_restful import  Api
from security import authenticate,identity
from user import UserRegister
from flask_jwt import JWT
from item import Itemlist,Item

app=Flask(__name__)
app.secret_key='vikas'
api=Api(app)

jwt=JWT(app,authenticate,identity)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Itemlist,'/items')
api.add_resource(UserRegister,'/register')

app.run(port=5000,debug=True)

