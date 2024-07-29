#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo http server for stub

import argparse
from flask import Flask, request, jsonify


def parse_args():
    parser = argparse.ArgumentParser(description='Start a Flask API to serve key-value data.')
    parser.add_argument('--data_file', '-d', type=str, default='demo.tsv', help='data file')
    args = parser.parse_args()
    return args


def load_data(file_path: str) -> dict:
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, values = line.strip().split('\t')
            data[key] = list(map(int, values.split(',')))
    return data


app = Flask(__name__)
args = parse_args()
data = load_data(args.data_file)


@app.route('/itemids', methods=['POST'])
def get_values():
    request_data = request.get_json()
    key = request_data.get('key')
    if key in data:
        return jsonify({'value': data[key]})
    else:
        return jsonify({'error': 'Key not found'}), 404


app.run(debug=True)
