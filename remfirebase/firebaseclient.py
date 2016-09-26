#!usr/bin/env python
#-*- coding: utf-8 -*-
from firebase import firebase

def init():
    return firebase.FirebaseApplication('https://rembot-68f41.firebaseio.com/', None)