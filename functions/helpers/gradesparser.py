#!usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup

import sys  
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

    def disciplines_grade_and_dict(self):
        disciplines_dict = {}
        soup = BeautifulSoup(self.get_grades_table(), 'lxml')
        disciplines = soup.findAll('tr')
        disciplines = str(disciplines).split('</tr>')[:-2]
        for discipline in disciplines[:-1]:
            discipline_soup = BeautifulSoup(discipline, 'lxml')
            discipline_name = discipline_soup.find('td', 'table-left').text
            disciplines_dict[discipline_name] = []
        return disciplines, disciplines_dict

    def parse_grades(self):
        grade_and_dict = self.disciplines_grade_and_dict()
        grades, disciplines_dict = grade_and_dict[0], grade_and_dict[1]   
        grades_matches = re.findall('\d{1,2},\d{2}', str(grades))
        print grades_matches
        # for x in range(len(grades_matches)):
            # print grades_matches[x]
            # print grades_matches[x+1]
            # print grades_matches[x+1]

        # print 'primeiro bimestre: {}\nsegundo bimestre: {}\nmedia final: {}'.format(
                # grades_matches[0],
                # grades_matches[1],
                # grades_matches[4]
            # )
        # print disciplines_dict

if __name__ == '__main__':
    ra = '1510512'
    senha = '147071'
    semestre = 3
    parser = GradesParser(ra, senha, semestre)
    parser.parse_grades()
    # print parser.disciplines_grade_and_dict()[1]   