#!usr/bin/env python
#-*- coding: utf-8 -*-

from remfirebase import classes 

def hello():
    """ Rem dirá hello """
    return 'hello'

def bye():
    """ Rem dirá bye """
    return 'bye'

def sala():
    """ Este comando irá retornar as salas onde a aula será lecionada no dia atual """
    salas = classes.getclasses()
    return 'primeiro horário: {}\nsegundo horário: {}'.format(salas['fclass'], salas['sclass'])

def help(command = ''):
    """ - hello\n- bye\n- sala """
    if not command == '':
        return globals()[command].__doc__
    elif command == '':
        return help.__doc__