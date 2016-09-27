#!usr/bin/env python
#-*- coding: utf-8 -*-

from config import settings
from slackclient import SlackClient

def initclient():
    print "Inicializando slackclient..."
    return SlackClient(settings.SLACK_BOT_TOKEN)
