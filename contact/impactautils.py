#!usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup
from firebase import firebase

reload(sys)
sys.setdefaultencoding('utf-8')

class ImpactaUtils(object):

    def __init__(self):
        self.session = requests.session()
        self.contact_dict = {}
        self.firebase_client = firebase.FirebaseApplication("https://rembot-68f41.firebaseio.com/", None)

    def execute(self):
        self.login()
        self.parse_contact_grade(self.get_contact_page())
        self.save_emails()

    def login(self):
        # Nrra: RA  -  Dessenha : SENHA 
        post_dict = { 'nrra': '', 'dessenha': '' }
        self.session.post("http://www.impacta.edu.br/account/enter.php", data=post_dict)

    def get_contact_page(self):
        return self.session.get("http://www.impacta.edu.br/aluno/contato-professores.php").text

    def parse_contact_grade(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        tr_list = soup.findAll('tr')
        tr_list.pop(0)
        for tr in tr_list:
            new_soup = BeautifulSoup(tr.prettify('utf-8'), 'html.parser')
            name = new_soup.find('td').text
            email = new_soup.find('td', 'emailprofessor').text
            self.contact_dict[name] = email.lower()

    def post_email_in_database(self, name, email):
        self.firebase_client.put("teachers_email", name, email)

    def save_emails(self):
        for teacher in self.contact_dict:
            self.post_email_in_database(teacher.strip() , self.contact_dict[teacher].strip())
