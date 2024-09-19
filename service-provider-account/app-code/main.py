from flask import Flask, jsonify, make_response
import json
main = Flask(__name__)


@main.route("/")
def hello_world():
    return make_response(jsonify("Hello, World!"),200)

@main.route("/customers")
def hello_customers():
  return make_response(json.dumps(
      { 'message': 'This is a private API of customers', 'data': [
    {
      'id': 1,
      'name': 'Michael Jordon',
      'Designation': 'Quality Assurance Engineer'
    },
    {
      'id': 2,
      'name': 'John Doe',
      'Designation': 'Account Manager'
    },
    {
      'id': 3,
      'name': 'Steve Smith',
      'Designation': 'Sales Representative'
    }
  ]}),200)

@main.route("/products")
def hello_products():
  return make_response(json.dumps(
      { 'message': 'This is a private API for products', 'data': [
    {
      'id': 1,
      'name': 'Stylish Cup',
      'price': 35,
      'currency': 'USD'
    },
    {
      'id': 2,
      'name': 'Water Bottle',
      'price': 58,
      'currency': 'USD'
    },
    {
      'id': 3,
      'name': 'Wooden Table',
      'price': 350,
      'currency': 'USD'
    }
  ]}),200)
  
main.run(host="0.0.0.0",port=5000)