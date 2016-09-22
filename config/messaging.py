#!usr/bin/env python
#-*- coding: utf-8 -*-
import requests
import connection

def main():
    sendmessage('hello')

def sendmessage(message):
    requests.post(connection.connect(), data = {'type': message})

if __name__ == '__main__':
    main()