#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-05-04 17:24:11
# @Last Modified by:   yhf
# @Last Modified time: 2015-05-11 15:44:38

from flask import request, render_template
from mysite import app
import requests


@app.route("/search", methods=['GET'])
def search():
    text = request.args.get('q')
    r = requests.get('http://localhost:9200/jdbc/_search?q=text:%s' % text)
    data = r.json()
    if data.get('error', None):
        return "no result"
    items = data['hits']['hits']
    ret = [item['_source'] for item in items if item['_score'] >= 0.1]
    return render_template('search.html', articles=ret)
