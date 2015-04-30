#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-04-13 18:53:53
# @Last Modified by:   yhf
# @Last Modified time: 2015-04-30 23:04:39

from flask import render_template
from mysite import app
from mysite.models.article import Article


NUM_ARTICLES_PER_PAGE = 50


@app.route("/")
def index():
    articles = Article.query.with_entities(Article.id, Article.title, Article.time).limit(NUM_ARTICLES_PER_PAGE).all()
    return render_template('index.html', articles=articles, page_num=1)


@app.route("/page/<int:page_num>")
def page(page_num):
    offset = (page_num - 1) * NUM_ARTICLES_PER_PAGE
    articles = Article.query.with_entities(Article.id, Article.title, Article.time).offset(offset).limit(NUM_ARTICLES_PER_PAGE)
    if not len(list(articles)):
        return render_template('404.html'), 404
    return render_template('index.html', articles=articles, page_num=page_num)


@app.route("/article/<int:article_id>", methods=['GET'])
def article(article_id):
    return Article.query.filter_by(id=article_id).all()[0].text
