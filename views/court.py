#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-05-03 22:49:20
# @Last Modified by:   yhf
# @Last Modified time: 2015-05-11 16:08:36

from flask import render_template
from sqlalchemy.sql import func
from mysite import app, db
from mysite.model.article import Article
from mysite.views.index import NUM_ARTICLES_PER_PAGE


NUM_COURTS_PER_PAGE = 30


@app.route('/court/', defaults={'page_num': 1})
@app.route("/court/page/<int:page_num>")
def court_page(page_num):
    """法院的排行
    """
    offset = (page_num - 1) * NUM_COURTS_PER_PAGE
    courts = db.session.query(Article.court, func.count(Article.court).label('c')).\
        group_by(Article.court).order_by('c DESC').offset(offset).limit(NUM_COURTS_PER_PAGE)
    if not len(list(courts)):
        return render_template('404.html'), 404
    return render_template('court.html', courts=courts, page_num=page_num)


@app.route('/court/<court_name>/', defaults={'page_num': 1})
@app.route("/court/<court_name>/page/<int:page_num>", methods=['GET'])
def court_home_page(court_name, page_num):
    """法院的主页
    """
    offset = (page_num - 1) * NUM_ARTICLES_PER_PAGE
    court_name = court_name.encode('utf-8')
    articles = Article.query.filter_by(court=court_name).offset(offset).limit(NUM_ARTICLES_PER_PAGE)\
        .with_entities(Article.id, Article.title, Article.time).all()
    if not len(list(articles)):
        return render_template('404.html'), 404
    return render_template('articles.html', articles=articles, page_num=page_num,
        court=True, court_name=court_name)

