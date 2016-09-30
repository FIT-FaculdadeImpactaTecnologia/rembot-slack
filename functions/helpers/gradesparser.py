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
        chunked_list = [grades_matches[x:x+5] for x in xrange(0, len(grades_matches), 5)]
        
        for discipline_grade in chunked_list:
            for discipline in disciplines_dict:
                disciplines_dict[discipline] = chunked_list.pop()

        return disciplines_dict

    def bot_response(self):
        response_string = "Aqui estão suas notas\n"
        disciplines_grades = self.parse_grades()
        for discipline in disciplines_grades:
            response_string += ":books:{}:\n:one: : {}\n:two: : {}\nFINAL: {}\n".format(discipline, disciplines_grades[discipline][0], disciplines_grades[discipline][1], disciplines_grades[discipline][-1])

        return response_string