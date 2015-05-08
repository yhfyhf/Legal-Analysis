# encoding: utf-8
from flask import Flask
# from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# api = restful.Api(app)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://%s:%s@%s/%s" % ("yhf", "123", "localhost:3306", "legal")

db = SQLAlchemy(app)

from mysite.views import index
from mysite.views import article
from mysite.views import court
from mysite.views import search

from mysite.api import courts
from mysite.api import articles
