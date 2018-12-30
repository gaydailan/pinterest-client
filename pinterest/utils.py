# -*- coding: utf-8 -*-
import urllib
from six import string_types


def url_encode(query):
    if isinstance(query, string_types):
        query = urllib.quote_plus(query)
    else:
        query = urllib.urlencode(query)
    query = query.replace('+', '%20')
    return query
