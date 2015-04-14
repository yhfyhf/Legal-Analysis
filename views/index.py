#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-04-13 18:53:53
# @Last Modified by:   yhf
# @Last Modified time: 2015-04-14 22:59:01

from flask import render_template
from mysite import app
from mysite.models.article import Article


@app.route("/")
def hello():
    articles = Article.query.with_entities(Article.id, Article.title, Article.time).limit(10).all()
    return render_template('index.html', articles=articles)


@app.route("/article/<int:article_id>", methods=['GET'])
def article(article_id):
    return Article.query.filter_by(id=article_id).all()[0].text
