#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-05-10 20:58:38
# @Last Modified by:   yhf
# @Last Modified time: 2015-05-11 16:11:34

from flask import request, jsonify
from mysite import app
from mysite.api import CONTENTTYPE
import requests


@app.route("/api/search/", methods=['GET'])
def search_api():
    query = request.args.get('title')
    if query:
        r = requests.get('http://localhost:9200/jdbc/_search?q=title:%s' % query)
    else:
        query = request.args.get('text')
        r = requests.get('http://localhost:9200/jdbc/_search?q=text:%s' % query)
    data = r.json()
    if data.get('error', None):
        return jsonify({"error": "search error"}), 200, CONTENTTYPE
    else:
        items = data['hits']['hits']
        ret = [item['_source'] for item in items if item['_score'] >= 0.1]
        return jsonify({"articles": ret}), 200, CONTENTTYPE
