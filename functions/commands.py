#!usr/bin/env python
#-*- coding: utf-8 -*-

from remfirebase import classes 

def traduzir():
    return 'função em desenvolvimento!'

def sala():
    salas = classes.getclasses()
    return ':clock7:  {}\n:clock9:  {}\n'.format(salas['fclass'], salas['sclass'])


def help(command = ''):
    if not command == '':
        return globals()[command].__doc__
    else:
        return help.__doc__
