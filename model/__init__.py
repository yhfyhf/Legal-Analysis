#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yhf
# @Date:   2015-04-13 19:19:54
# @Last Modified by:   yhf
# @Last Modified time: 2015-05-08 09:19:26

from datetime import datetime


class SerializableModel(object):
    """ A SQLAlchemy model mixin class that can serialize itself as JSON. """

    def to_dict(self):
        """Return dict representation of class by iterating over database columns."""
        value = {}
        for column in self.__table__.columns:
            attribute = getattr(self, column.name)
            if isinstance(attribute, datetime):
                attribute = str(attribute)
            value[column.name] = attribute
        return value
