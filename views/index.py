#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-04-13 18:53:53
# @Last Modified by:   yhf
# @Last Modified time: 2015-05-04 23:49:33

from flask import render_template
from sqlalchemy.sql import func
from mysite import app, db
from mysite.models.article import Article


NUM_ARTICLES_PER_PAGE = 50
NUM_COURTS_PER_PAGE = 50

@app.route("/")
def index():
    """首页
    """
    articles = Article.query.with_entities(Article.id, Article.title, Article.time).limit(NUM_ARTICLES_PER_PAGE).all()
    courts = db.session.query(Article.court, func.count(Article.court).label('c')).\
        group_by(Article.court).order_by('c DESC').limit(NUM_COURTS_PER_PAGE)
    print "*" * 20
    print zip(articles, courts)[0]
    print "*" * 20
    return render_template('index.html', zip=zip(articles, courts))


@app.route("/page/<int:page_num>")
def articles(page_num):
    offset = (page_num - 1) * NUM_ARTICLES_PER_PAGE
    articles = Article.query.with_entities(Article.id, Article.title, Article.time).offset(offset).limit(NUM_ARTICLES_PER_PAGE)
    if not len(list(articles)):
        return render_template('404.html'), 404
    return render_template('articles.html', articles=articles, page_num=page_num)
