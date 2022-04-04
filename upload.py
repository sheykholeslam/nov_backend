# coding=utf8
import pandas as pd
from model import *

def parse_csv(file_path, metric_codes):
    col_names = ['metric_code','metric_description','value_label', 'value_type']
    rows = pd.read_csv(file_path, names=col_names, header=1)
    for i,row in rows.iterrows():
        if 'metric_code' in row and 'metric_description' in row:
            metric_code = row['metric_code']
            metric_description = row['metric_description']
            metric = Metric.query.filter_by(code=metric_code).first()
            if metric is None:
                metric = add_metric(metric_code, metric_description)

            if 'value_label' in row and 'value_type' in row:
                value_label = row['value_label']
                value_type = row['value_type']
                add_definition(value_label, value_type, metric.id)

def add_metric(metric_code, metric_description):
    metric = Metric(code=metric_code, description=metric_description)
    db.session.add(metric)
    db.session.commit()
    return metric

def add_definition(value_label, value_type, metric_id):
    definition = ValueDefinition(metric_id=metric_id, label=value_label, type=value_type)
    db.session.add(definition)
    db.session.commit()
    return definition
