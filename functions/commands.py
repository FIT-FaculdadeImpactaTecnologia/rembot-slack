#!usr/bin/env python
#-*- coding: utf-8 -*-

from helpers.gradesparser import GradesParser
from remfirebase import classes
from contact.searcher import Searcher

def traduzir():
    return 'função em desenvolvimento!'

def sala(params = []):
    if(len(params) == 2):
        salas = classes.getclasses(params)
        return ':clock7:  {}\n:clock9:  {}\n'.format(salas['fclass'], salas['sclass'])
    else:
        return 'Parâmetros inválidos :exclamation:'

def notas(params = []):
    if(len(params) == 3):
        grades = GradesParser(params[0], params[1], params[2])
        return grades.bot_exec()
    else:
        return 'Parâmetros inválidos:exclamation:'

def professor(params = []):
    if(len(params) == 1):
        name = '{}'.format(params[0])
        searcher = Searcher(name)
        return searcher.search()
    else:
        return 'Parâmetros inválidos:exclamation:'

def help(command = ''):
    """
/sala
/notas @ ra senha semestre
    """
    return help.__doc__
