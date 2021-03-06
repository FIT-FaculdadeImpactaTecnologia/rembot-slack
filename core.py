#!usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import time
from config import settings
from functions import parser
from functions import handler 
from functions import initializer 
from slackclient import SlackClient

reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    print "Inicializando rembot..."
    client = initializer.initclient()
    READ_WEBSOCKET_DELAY = 3
    if client.rtm_connect():
        print "Rembot connected and running!"
        while True:
            command, channel = parser.parse_slack_output(client.rtm_read())
            if command and channel:
                handler.handle_command(command, channel)
                time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print "Connection failed. Invalid token or bot ID"

if __name__ == '__main__':
    main()