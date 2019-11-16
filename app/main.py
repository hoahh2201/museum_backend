"""
This module is the main flask application.
"""


import firebase_admin
from flask import Flask, request
import json
from blueprints import *
from google.cloud import firestore 
from models import product_catalog
import jsonpickle
#from helpers import firestore_client
# Initialize Firebase Admin SDK.
# See https://firebase.google.com/docs/admin/setup for more information.
firebase = firebase_admin.initialize_app()
firestore_client = firestore.Client()
app = Flask(__name__)
app.secret_key = b'A Super Secret Key'


app.register_blueprint(home_page)

@app.route("/search/", methods=["POST"])
def search():
    val = request.get_data()
    val = str(request.get_data())
    val1=val[2:-1]
    products = firestore_client.collection('products').where("place", "==", val1).get()
    products = firestore_client.collection('products').where("name", ">=", val1).get()

    product_list = [product_catalog.data_classes.Product.deserialize(product) for product in list(products)]

    return jsonpickle.encode({'product_list':product_list,'bucket':product_catalog.BUCKET})

if __name__ == '__main__':
    app.run(debug=True)