#!usr/bin/env python
#-*- coding: utf-8 -*-
import settings
import requests

def connect():
    rtm = initrtm()
    return rtm['url']

def initrtm():
    connection_response = requests.post('https://slack.com/api/rtm.start', data = {'token': settings.API_TOKEN})
    return connection_response.json()