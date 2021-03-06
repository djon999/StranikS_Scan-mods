﻿# -*- coding: utf-8 -*-

import json, urllib2

STATUS_ERRORS = frozenset(['error', 'badRequest', 'badToken'])

def loadUrl(request):
    try:
        response = urllib2.urlopen(request)
        if response.code == 200:
            return response.read()
    except:
        pass

def loadJsonUrl(request):
    stats = loadUrl(request)
    if stats:
        try:
            stats = json.loads(stats)
        except:
            pass
        else:
            if isinstance(stats, dict):
                return stats if stats.get('status', '') not in STATUS_ERRORS else {}
