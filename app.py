# coding=utf8
from flask import Flask, escape, request, render_template, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
import os
from os.path import join, dirname, realpath
import pandas as pd

from model import *
from upload import parse_csv

def create_app():
    app = Flask(__name__)
    UPLOAD_FOLDER = 'uploads'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    db.init_app(app)
    ma.init_app(app)
    return app

app =create_app()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        metric_code = request.form['code']
        metric_desc = request.form['description']
        new_metric = request.form['code'] = MetricSchema(code = metric_code, description= metric_desc)
        try:
            db.session.add(new_metric)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue creating metric'
    else: 
        metrics = Metric.query.all()
        value_definitions = ValueDefinition.query.all()
        return render_template('index.html', metrics = metrics, value_definitions= value_definitions)


@app.route('/metrics', methods=['GET'])
def get_metrics():
    metrics = Metric.query.all()
    result = metrics_schema.dump(metrics)
    return jsonify(result)

@app.route('/definitions', methods=['GET'])
def get_value_definitions():
    value_definitions = ValueDefinition.query.all()
    result = value_definitions_schema.dump(value_definitions)
    return jsonify(result)

@app.route('/upload-csv', methods=['GET', 'POST'])
def load_csv():
    if request.method == 'POST':
        uploaded_file = request.files['csv_file']
        file_name = uploaded_file.filename
        if file_name != '':
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
            metric_dump = metric_codes_schema.dump(Metric.query.all())
            metric_codes = [x['code'] for x in metric_dump]
            try:
                parse_csv(file_path, metric_codes)
                return redirect('/')
            except Exception as e:
                print('ERROR:', e)
                return 'There was an issue parsing the csv file'
    else:
        return render_template('upload_csv.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)



