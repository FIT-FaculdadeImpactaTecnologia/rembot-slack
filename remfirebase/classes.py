#!usr/bin/env python
#-*- coding: utf-8 -*-
import time
import firebaseclient

day = time.strftime("%A").lower()

def getclasses(params):
    path = '/{}/{}/{}'.format(params[0].lower(), params[1], day)
    client = firebaseclient.init()
    return client.get(path, None)