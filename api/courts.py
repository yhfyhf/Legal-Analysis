#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-05-08 00:00:24
# @Last Modified by:   yhf
# @Last Modified time: 2015-05-08 09:19:14

from flask import request, jsonify
from sqlalchemy.sql import func
from mysite import app, db
from mysite.model.article import Article
from mysite.views.index import NUM_COURTS_PER_PAGE
from mysite.api import CONTENTTYPE


@app.route("/api/courts")
def courts():
    """ Returns a list of courts.
    """
    limit = request.args.get('limit') or NUM_COURTS_PER_PAGE
    offset = request.args.get('offset') or 0
    sortby = request.args.get('sortby') or 'desc'
    courts = db.session.query(Article.court, func.count(Article.court).label('c')).\
        group_by(Article.court).order_by('c '+sortby).offset(offset).limit(limit)
    courts = [{"court": c[0], "count": c[1]} for c in courts]
    ret = jsonify({
            "limit": limit,
            "offset": offset,
            "sortby": sortby,
            "courts": courts,
        })
    return ret, 200, CONTENTTYPE
