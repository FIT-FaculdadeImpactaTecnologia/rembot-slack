#!usr/bin/env python
#-*- coding: utf-8 -*-
import time
import firebaseclient

day = time.strftime("%A").lower()

def getclasses():
    client = firebaseclient.init()
    return client.get('/' + str(day), None)