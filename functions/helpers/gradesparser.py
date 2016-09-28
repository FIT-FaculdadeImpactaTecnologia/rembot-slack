#!usr/bin/env python
#-*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

class GradesParser(object):

    def __init__(self, ra, password, semester):
        self.grades = []
        self.ra = ra
        self.password = password
        self.session = requests.session()
        self.semester = semester
        self.login_url = 'http://www.impacta.edu.br/account/enter.php'
        self.grades_url = 'http://www.impacta.edu.br/aluno/'

    def login(self):
        login_data = {'nrra': self.ra,'dessenha': self.password}
        return self.session.post(self.login_url, data=login_data)

    def getgradesurl(self):
        self.login()
        grades_soup = BeautifulSoup(self.session.get(self.grades_url + 'notas-faltas.php').text, 'lxml')
        grades_table = grades_soup.find(id = 'grid-cursos-notas-faltas').findAll('tr')
        for section in grades_table:
            section_soup = BeautifulSoup(str(section), 'lxml')
            semester = section_soup.findAll('td')[4].text[:1]
            if int(semester) == self.semester:
                return section_soup.find('a')['href']

    def getgradestable(self):
        response = self.session.get(self.grades_url + self.getgradesurl())
        return response.text

if __name__ == '__main__':
    ra = 'xxxxxx'
    senha = 'xxxxxx'
    semestre = 3
    parser = GradesParser(ra, senha, semestre)
    print parser.getgradestable()