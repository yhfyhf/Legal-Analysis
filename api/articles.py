#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-05-08 08:57:06
# @Last Modified by:   yhf
# @Last Modified time: 2015-05-08 09:24:16

from flask import request, jsonify
from mysite import app
from mysite.model.article import Article
from mysite.views.index import NUM_ARTICLES_PER_PAGE
from mysite.api import CONTENTTYPE


@app.route("/api/articles/", methods=['GET'])
def articles():
    """ Returns a list of articles.
    """
    limit = request.args.get('limit') or NUM_ARTICLES_PER_PAGE
    offset = request.args.get('offset') or 0
    sortby = request.args.get('sortby') or 'desc'
    court = request.args.get('court') or None
    court = court.encode('utf-8')
    if court:
        articles = Article.query.filter_by(court=court).order_by('id '+sortby).offset(offset).limit(limit).all()
        total = Article.query.filter_by(court=court).count()
    else:
        articles = Article.query.order_by('id '+sortby).offset(offset).limit(limit).all()
        total = Article.query.count()
    ret = jsonify({
            "total": total,
            "limit": limit,
            "offset": offset,
            "sortby": sortby,
            "articles": [a.to_dict() for a in articles]
        })
    return ret, 200, CONTENTTYPE
