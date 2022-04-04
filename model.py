# coding=utf8
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

db = SQLAlchemy()
ma = Marshmallow()

class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)

class MetricSchema(ma.Schema):
  class Meta:
    fields = ('id', 'code', 'description')

metric_schema = MetricSchema()
metrics_schema = MetricSchema(many=True)
metric_codes_schema = MetricSchema(many=True, only=['code'])

class ValueDefinition(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(200), nullable=False)
    metric_id = db.Column(db.Integer, db.ForeignKey('metric.id'), nullable = False)
    metric = db.relationship("Metric", backref="value_definitions")

class ValueDefinitionSchema(ma.Schema):
    metric = ma.Nested(MetricSchema, dump_only=True)
    class Meta:
        fields = ('id', 'label', 'type', 'metric')

value_definition_schema = ValueDefinitionSchema()
value_definitions_schema = ValueDefinitionSchema(many=True)