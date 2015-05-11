#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-05-08 08:57:06
# @Last Modified by:   yhf
# @Last Modified time: 2015-05-08 09:34:12

from flask import request, jsonify
from sqlalchemy.sql import func
from mysite import app, db
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
    if court:
        court = court.encode('utf-8')
        articles = Article.query.filter_by(court=court).order_by('id '+sortby).offset(offset).limit(limit).all()
        total = Article.query.filter_by(court=court).count()
    else:
        articles = Article.query.order_by('id '+sortby).offset(offset).limit(limit).all()
        total = db.session.query(func.count(Article.id)).one()[0]
    ret = jsonify({
            "total": total,
            "limit": limit,
            "offset": offset,
            "sortby": sortby,
            "articles": [a.to_dict() for a in articles]
        })
    return ret, 200, CONTENTTYPE
