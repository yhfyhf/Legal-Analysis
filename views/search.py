#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-05-04 17:24:11
# @Last Modified by:   yhf
# @Last Modified time: 2015-05-04 22:06:36

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
    ret = list()
    for item in items:
        if (item['_score'] < 0.1):
            continue
        print len(item['_source'])
        ret.append(item['_source'])
    return render_template('search.html', articles=ret)
