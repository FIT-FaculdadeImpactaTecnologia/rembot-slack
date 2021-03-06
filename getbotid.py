#!usr/bin/env python
#-*- coding: utf-8 -*-

from config import settings
from slackclient import SlackClient

def getBotId():
    client = SlackClient(settings.SLACK_BOT_TOKEN)
    api_call = client.api_call('users.list')
    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            if user.get('name') == settings.SLACK_BOT_NAME:
                print user.get('id')
            else:
                print "não foi possível recuperar o id do bot"

if __name__ == '__main__':
    getBotId()
