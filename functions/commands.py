#!usr/bin/env python
#-*- coding: utf-8 -*-

from helpers.gradesparser import GradesParser
from remfirebase import classes 

def traduzir():
    return 'função em desenvolvimento!'

def sala():
    salas = classes.getclasses()
    return ':clock7:  {}\n:clock9:  {}\n'.format(salas['fclass'], salas['sclass'])

def notas(params = []):
    if(len(params) == 3):
        grades = GradesParser(params[0], params[1], params[2])
        return grades.bot_exec()
    else:
        return 'Parâmetros inválidos:exclamation:'

def help(command = ''):
    """
/sala
/notas @ ra senha semestre
/traduzir
    """
    return help.__doc__
