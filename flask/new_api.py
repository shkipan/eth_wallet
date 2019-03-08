#!/usr/bin/env python

import flask, requests, struct, sys
from flask import json, jsonify, request, make_response, url_for, render_template
from time import time, sleep, gmtime, strftime
from pathlib import Path
import threading
from web3 import Web3


app = flask.Flask(__name__)
app.config["DEBUG"] = True
w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/79852596bc8f47348e59e2577716f7bb"))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#home page, default route
@app.route('/', methods=['GET'])
def homepage():
    return render_template('home.html', title = 'Home page', data=0), 201

#home page, default route
@app.route('/address', methods=['GET'])
def get_address():
    addr = request.args.get('address')
    if not addr or not w3.isAddress(addr):
        return render_template('table.html', title = 'Table page', data=[-42]), 201
    x = "{:.3f}".format(w3.fromWei(w3.eth.getBalance(addr), 'ether'))
    return render_template('table.html', title = 'Table page', data=[x,2,3,4,5]), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242, threaded=True)

