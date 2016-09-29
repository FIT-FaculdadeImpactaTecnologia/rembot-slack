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

    def get_grades_url(self):
        self.login()
        grades_soup = BeautifulSoup(self.session.get(self.grades_url + 'notas-faltas.php').text, 'html.parser')
        grades_soup = BeautifulSoup(self.session.get(self.grades_url + 'notas-faltas.php').text, 'html.parser')
        grades_table = grades_soup.find(id = 'grid-cursos-notas-faltas').findAll('tr')
        for section in grades_table:
            section_soup = BeautifulSoup(str(section), 'lxml')
            semester = section_soup.findAll('td')[4].text[:1]
            if int(semester) == self.semester:
                return section_soup.find('a')['href']

    def find_grade_grid(self, s):
         grandes_start_index = s.find('<th class="table-subtitle">Situa')
         grades_end_index = s.find('<div class="legends container well pull-left">')
         return s[grandes_start_index:grades_end_index]

    def get_grades_table(self):
        response = self.session.get(self.grades_url + self.get_grades_url())
        grades_grid = self.find_grade_grid(response.text)
        return grades_grid

    def parse_grades_table(self):
        soup = BeautifulSoup(self.get_grades_table(), 'lxml')
        # print soup.prettify()
        disciplines = soup.findAll('tr')
        disciplines = str(disciplines).split('</tr>')
        print disciplines[-1]
        # for discipline in disciplines[:-1]:
            # discipline_soup = BeautifulSoup(discipline, 'lxml')
            # print discipline_soup.find('td', 'table-left').text

if __name__ == '__main__':
    ra = '1510512'
    senha = '147071'
    semestre = 3
    parser = GradesParser(ra, senha, semestre)
    parser.parse_grades_table()   