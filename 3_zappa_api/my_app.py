import json
from flask import Flask
app = Flask(__name__)
import pymysql
import datetime

from _functions import _get_importer, _get_importer_products, _get_importer_similar, _get_similar_importer_products
from _functions import _get_product , _get_product_importers

@app.route('/')
def hello_world():
    return "Welcome to my API"

### importers
@app.route('/importer/<int:importer_id>', methods = ['GET'])
def get_importer(importer_id):
    return _get_importer._get_importer(importer_id)


@app.route('/importer/<int:importer_id>/products', methods = ['GET'])
def get_importer_products(importer_id):
    return _get_importer_products._get_importer_products(importer_id)


@app.route('/importer/<int:importer_id>/similar', methods = ['GET'])
def get_importer_similar(importer_id):
    return _get_importer_similar._get_importer_similar(importer_id)

@app.route('/importer/<int:importer_id>/similar/products', methods = ['GET'])
def get_similar_importer_products(importer_id):
    return _get_similar_importer_products._get_similar_importer_products(importer_id)


### products
@app.route('/product/<product_id>', methods = ['GET'])
def get_product(product_id):
    return _get_product._get_product(product_id)


@app.route('/product/<product_id>/importers', methods = ['GET'])
def get_product_importers(product_id):
    return _get_product_importers._get_product_importers(product_id)


### ping
@app.route('/ping')
def ping():
    return "pong", 200