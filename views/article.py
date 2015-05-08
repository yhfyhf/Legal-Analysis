#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-05-03 22:02:06
# @Last Modified by:   yhf
# @Last Modified time: 2015-05-08 08:00:22

from flask import render_template
from mysite import app
from mysite.model.article import Article


@app.route("/article/<int:article_id>", methods=['GET'])
def article(article_id):
    article = Article.query.filter_by(id=article_id).all()[0]
    items = article.text.split('\n')
    article.type = items[1]
    article.number = items[2]
    article.text = '\n'.join(items[3:])
    return render_template('article.html', article=article)
