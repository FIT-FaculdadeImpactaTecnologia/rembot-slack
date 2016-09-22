#!usr/bin/env python
#-*- coding: utf-8 -*-
import websocket
from websocket import create_connection

import connection

def init():
    ws = create_connection(connection.geturl())
    print ws.recv()

init()