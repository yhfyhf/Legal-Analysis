#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-05-03 22:49:20
# @Last Modified by:   yhf
# @Last Modified time: 2015-05-03 23:31:03

from flask import render_template
from sqlalchemy.sql import func
from mysite import app, db
from mysite.models.article import Article


NUM_COURTS_PER_PAGE = 30


@app.route("/court")
def court_index():
    courts = db.session.query(Article.court, func.count(Article.court).label('c')).\
        group_by(Article.court).order_by('c DESC').limit(NUM_COURTS_PER_PAGE).all()
    return render_template('court.html', courts=courts, page_num=1)


@app.route("/court/page/<int:page_num>")
def court_page(page_num):
    offset = (page_num - 1) * NUM_COURTS_PER_PAGE
    courts = db.session.query(Article.court, func.count(Article.court).label('c')).\
        group_by(Article.court).order_by('c DESC').offset(offset).limit(NUM_COURTS_PER_PAGE)
    if not len(list(courts)):
        return render_template('404.html'), 404
    return render_template('court.html', courts=courts, page_num=page_num)


@app.route("/court/<court_name>", methods=['GET'])
def court(court_name):
    court_name = court_name.encode('utf-8')
    articles = Article.query.filter_by(court=court_name).with_entities(Article.id, Article.title, Article.time).all()
    return render_template('index.html', articles=articles)
