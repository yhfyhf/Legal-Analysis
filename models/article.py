#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-04-13 19:19:42
# @Last Modified by:   yhf
# @Last Modified time: 2015-04-13 23:29:40

from mysite import db


class Article(db.Model):

    __tablename__ = 'judgement'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120))
    title = db.Column(db.String(100))
    court = db.Column(db.String(100))
    time = db.Column(db.String(100))
    text = db.Column(db.String(10000))
